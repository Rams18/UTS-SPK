# UAS spk_web

## Install requirements

    pip install -r requirements.txt

## Run the app
to run the web app simply  use

    python main.py

## Usage
Install postman 
https://www.postman.com/downloads/

get susu list
<img src='img/Get_Susu.png' alt='susu list'/>

get recommendations saw
<img src='img/Post_saw.png' alt='recommendations saw'/>

get recommendations wp
<img src='img/Post_Wp.png' alt='recommendations wp'/>

### TUGAS UAS
Implementasikan model yang sudah anda buat ke dalam web api dengan http method `POST`

INPUT:
{
    "harga": 4, 
    "kalori": 3, 
    "protein": 4, 
    "lemak": 6, 
    "ukuran": 3
}

OUTPUT (diurutkan / sort dari yang terbesar ke yang terkecil):

post recommendations saw
<img src='img/Post_saw.png' alt='recommendations saw'/>

post recommendations wp
<img src='img/Post_Wp.png' alt='recommendations wp'/>
