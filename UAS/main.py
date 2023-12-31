
from http import HTTPStatus
from flask import Flask, request, abort
from flask_restful import Resource, Api 
from models import Susu as SusuModel
from engine import engine
from sqlalchemy import select
from sqlalchemy.orm import Session

session = Session(engine)

app = Flask(__name__)
api = Api(app)        

class BaseMethod():

    def __init__(self):
        self.raw_weight = {'harga': 4, 'kalori': 3, 'protein': 4, 'lemak': 6, 'ukuran': 3}

    @property
    def weight(self):
        total_weight = sum(self.raw_weight.values())
        return {k: round(v/total_weight, 2) for k, v in self.raw_weight.items()}

    @property
    def data(self):
        query = select(SusuModel.id_susu, SusuModel.harga, SusuModel.kalori, SusuModel.protein, SusuModel.lemak, SusuModel.ukuran)
        result = session.execute(query).fetchall()
        print(result)
        return [{'id_susu': susu.id_susu, 'harga': susu.harga, 'kalori': susu.kalori, 'protein': susu.protein, 'lemak': susu.lemak, 'ukuran': susu.ukuran} for susu in result]

    @property
    def normalized_data(self):
        harga_values = []
        kalori_values = []
        protein_values = []
        lemak_values = []
        ukuran_values = []

        for data in self.data:
            harga_values.append(data['harga'])
            kalori_values.append(data['kalori'])
            protein_values.append(data['protein'])
            lemak_values.append(data['lemak'])
            ukuran_values.append(data['ukuran'])

        return [
            {'id_susu': data['id_susu'],
             'harga': min(harga_values) / data['harga'],
             'kalori': data['kalori'] / max(kalori_values),
             'protein': data['protein'] / max(protein_values),
             'lemak': data['lemak'] / max(lemak_values),
             'ukuran': data['ukuran'] / max(ukuran_values)
             }
            for data in self.data
        ]

    def update_weights(self, new_weights):
        self.raw_weight = new_weights

class WeightedProductCalculator(BaseMethod):
    def update_weights(self, new_weights):
        self.raw_weight = new_weights

    @property
    def calculate(self):
        normalized_data = self.normalized_data
        produk = []

        for row in normalized_data:
            product_score = (
                row['harga'] ** self.raw_weight['harga'] *
                row['kalori'] ** self.raw_weight['kalori'] *
                row['protein'] ** self.raw_weight['protein'] *
                row['lemak'] ** self.raw_weight['lemak'] *
                row['ukuran'] ** self.raw_weight['ukuran']
            )

            produk.append({
                'id_susu': row['id_susu'],
                'produk': product_score
            })

        sorted_produk = sorted(produk, key=lambda x: x['produk'], reverse=True)

        sorted_data = []

        for product in sorted_produk:
            sorted_data.append({
                'id_susu': product['id_susu'],
                'score': product['produk']
            })

        return sorted_data


class WeightedProduct(Resource):
    def get(self):
        calculator = WeightedProductCalculator()
        result = calculator.calculate
        return result, HTTPStatus.OK.value
    
    def post(self):
        new_weights = request.get_json()
        calculator = WeightedProductCalculator()
        calculator.update_weights(new_weights)
        result = calculator.calculate
        return {'data': result}, HTTPStatus.OK.value
    

class SimpleAdditiveWeightingCalculator(BaseMethod):
    @property
    def calculate(self):
        weight = self.weight
        result = {row['id_susu']:
                  round(row['harga'] * weight['harga'] +
                        row['kalori'] * weight['kalori'] +
                        row['protein'] * weight['protein'] +
                        row['lemak'] * weight['lemak'] +
                        row['ukuran'] * weight['ukuran'], 2)
                  for row in self.normalized_data
                  }
        sorted_result = dict(
            sorted(result.items(), key=lambda x: x[1], reverse=True))
        return sorted_result

    def update_weights(self, new_weights):
        self.raw_weight = new_weights

class SimpleAdditiveWeighting(Resource):
    def get(self):
        saw = SimpleAdditiveWeightingCalculator()
        result = saw.calculate
        return result, HTTPStatus.OK.value

    def post(self):
        new_weights = request.get_json()
        saw = SimpleAdditiveWeightingCalculator()
        saw.update_weights(new_weights)
        result = saw.calculate
        return {'data': result}, HTTPStatus.OK.value


class Susu(Resource):
    def get_paginated_result(self, url, list, args):
        page_size = int(args.get('page_size', 10))
        page = int(args.get('page', 1))
        page_count = int((len(list) + page_size - 1) / page_size)
        start = (page - 1) * page_size
        end = min(start + page_size, len(list))

        if page < page_count:
            next_page = f'{url}?page={page+1}&page_size={page_size}'
        else:
            next_page = None
        if page > 1:
            prev_page = f'{url}?page={page-1}&page_size={page_size}'
        else:
            prev_page = None
        
        if page > page_count or page < 1:
            abort(404, description=f'Halaman {page} tidak ditemukan.') 
        return {
            'page': page, 
            'page_size': page_size,
            'next': next_page, 
            'prev': prev_page,
            'Results': list[start:end]
        }

    def get(self):
        query = select(SusuModel)
        data = [{'id_susu': susu.id_susu, 'harga': susu.harga, 'kalori': susu.kalori, 'protein': susu.protein, 'lemak': susu.lemak, 'ukuran': susu.ukuran} for susu in session.scalars(query)]
        return self.get_paginated_result('susu/', data, request.args), HTTPStatus.OK.value


api.add_resource(Susu, '/susu')
api.add_resource(WeightedProduct, '/wp')
api.add_resource(SimpleAdditiveWeighting, '/saw')

if __name__ == '__main__':
    app.run(port='5005', debug=True)
