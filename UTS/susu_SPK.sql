PGDMP     	    +    	        	    {            susu    10.23    10.23 
    �
           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                       false            �
           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                       false            �
           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                       false            �
           1262    16426    susu    DATABASE     �   CREATE DATABASE susu WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'English_Indonesia.1252' LC_CTYPE = 'English_Indonesia.1252';
    DROP DATABASE susu;
             postgres    false                        2615    2200    public    SCHEMA        CREATE SCHEMA public;
    DROP SCHEMA public;
             postgres    false            �
           0    0    SCHEMA public    COMMENT     6   COMMENT ON SCHEMA public IS 'standard public schema';
                  postgres    false    3                        3079    12924    plpgsql 	   EXTENSION     ?   CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;
    DROP EXTENSION plpgsql;
                  false            �
           0    0    EXTENSION plpgsql    COMMENT     @   COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';
                       false    1            �            1259    16427    susu    TABLE     �   CREATE TABLE public.susu (
    id_susu character varying NOT NULL,
    harga integer NOT NULL,
    kalori character varying NOT NULL,
    protein character varying NOT NULL,
    lemak character varying NOT NULL,
    ukuran character varying NOT NULL
);
    DROP TABLE public.susu;
       public         postgres    false    3            �
          0    16427    susu 
   TABLE DATA               N   COPY public.susu (id_susu, harga, kalori, protein, lemak, ukuran) FROM stdin;
    public       postgres    false    196   k       �
   x   x�%��D!c��}>0G���2!�<�5x�*,V�[IꊃDBu~(*"w�w6����x���ɣF���a��phUY�.�i�(��� ^�P:�	���;�����#     