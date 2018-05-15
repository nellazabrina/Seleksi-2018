<h1 align="center">
  <br>
  Tugas 1 Seleksi Warga Basdat 2018
  <br>
  <br>
</h1>

<h2 align="center">
  <br>
  Data Scraping
  <br>
  <br>
</h2>

### Deskripsi

Tugas ini dibuat dengan menggunakan bahasa python3 untuk melakukan scraping pada suatu website. Pada scraper ini, saya melakukan scraping di website "https://www.cari-kos.com/". Saya hanya mengambil 10 data dari tiap daerah yaitu (bali, di yogyakarta, dki jakarta, kota bandung, kota malang, dan kota surabaya) dengan melakukan sleep tiap scraping.

### Specifications

1. Lakukan data scraping dari sebuah laman web untuk memeroleh data atau informasi tertentu __TANPA MENGGUNAKAN API__

2. Peserta juga diminta untuk membuat Makefile sesuai template yang disediakan, sehingga program dengan gampang di-_build_, di-_run_, dan di-_clean_

3. Hasil data scraping ini nantinya akan digunakan sebagai bahan tugas analisis dan visualisasi data

### How to use
Cara menggunakannya adalah dengan merun file python yang ada (python3 scraper.py) kemudian file akan langsung melakukan scraping pada website tersebut.

### JSON Structure
JSON file dibuat untuk tiap kota dengan format
{nama kos: harga}

### Documentation

![Screenshot](/Tugas1/screenshots/data bali.jpg)

### Reference

import py_compile
from bs4 import BeautifulSoup
import urllib.request
import json
import time

### Author
Nella Zabrina

### Credit
terima kasih untuk website "https://www.cari-kos.com/"

<h1 align="center">
  <br>
  Selamat BerEksplorasi!
  <br>
  <br>
</h1>

<p align="center">
  <br>
  Basdat Industries - Lab Basdat 2018
  <br>
  <br>
</p>
