PGDMP                      {            SUSU    16.0    16.0     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    24706    SUSU    DATABASE     }   CREATE DATABASE "SUSU" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_Indonesia.1252';
    DROP DATABASE "SUSU";
                postgres    false                        2615    2200    public    SCHEMA        CREATE SCHEMA public;
    DROP SCHEMA public;
                postgres    false            �           0    0    SCHEMA public    COMMENT     6   COMMENT ON SCHEMA public IS 'standard public schema';
                   postgres    false    5            �            1259    24707    susu    TABLE     �   CREATE TABLE public.susu (
    id_susu character varying NOT NULL,
    harga integer NOT NULL,
    kalori integer NOT NULL,
    protein integer NOT NULL,
    lemak integer NOT NULL,
    ukuran integer NOT NULL
);
    DROP TABLE public.susu;
       public         heap    postgres    false    5            �          0    24707    susu 
   TABLE DATA           N   COPY public.susu (id_susu, harga, kalori, protein, lemak, ukuran) FROM stdin;
    public          postgres    false    215   �       �   x   x�%��D!c��}>0G���2!�<�5x�*,V�[IꊃDBu~(*"w�w6����x���ɣF���a��phUY�.�i�(��� ^�P:�	���;�����#     