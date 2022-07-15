# Deteksi Watermark dan Logo BI 
## Sebagai bagian dari Originalitas Mata Uang Rupiah

Project ini dikembangkan dari sumber berikut(https://github.com/rizanw/uang-matching.git)

Link Video presentasi dan Video Demo (GDrive)
https://drive.google.com/drive/u/1/folders/1fWbCHLvucFPTF4zB08Q-_zg4pX2QggDS

### Image Procesing Project.
Crazy Rich Team:
* Albert Sutandi
* Handinata
* Robert Carlos
* Michael Valiant

Cara kerjanya hanya mencocokan 2 Image yaitu Image Pembanding dengan Image yang di Uji.

### Library yang digunakan 
* import glob
* import cv2
* import numpy as np
* import imutils                  #Library yang sudah disediakan didalam project
* import tkinter
* from tkinter import messagebox  #Menampilkan Jendela Kotak Pesan dari atribute library tkinter
* import Main                     #Library untuk mengambil nilai variable yang ada di file Main.py

***Jika library numpy dan cv2 belum terinstal, bisa cari caranya di google***
Untuk project ini di jalankan dengan aplikasi Anaconda Navigator dengan editor Visual studio Code. 

### Terdapat 4 file pithon.
* WaterMarkDetection.py => Untuk melakukan deteksi watermark dari uang kertas Rupiah
* LogoDetection.py      => Untuk Melakukan deteksi Logo BI yang ada di Uang kertas Rupiah
* imutils.py            => Di file ini berisi beberapa fungsi yang digunakan pada file WaterMarkDetection & file LogoDetection.
* Main.py               => File ini merupakan file utama untuk menjalankan seluruh file diatas. 

### Terdapat 2 Folder
* Folder Template => Berisikan file image pembanding (Training Image) sebagai image pembanding untuk menyatakan
  uang kertas asli atau tidak.
* Folder Test => Berisikan file image uang kertas yang akan di uji keaslianya.

### Ket:
FIle pada folder Test terdapat 2 jenis fk (palsu), ori (asli)
FIle fk adalah file image asli namun sudah di edit pada bagian watermark dan logo
* Fk1-2k.jpg => watermark dihapus setengah dan logo BI di putar ke kiri 10 drajat dari yang asli.
* fk2-2k.jpg => watermark sepenuhnya dihapus, atau tanpa watermark dan logo BI tetap.
Catatan: Edit file uang pecahan 2000 tersebut hanya untuk pengujian sebagai uang palsu.

Setiap pecahan uang Rupiah memiliki watermark dan Latar dari logo Bi yang berbeda,
jadi dapat digunakan untuk melakukan penyesuaian guna mendeteksi originalitas dari uang pecahan tersebut.

=========================================================================

### Sukses:
* Watermark hanya terdeteksi dengan pecahan uang yang sama.
* Logo hanya terdeteksi dengan pecahan uang yang sama.

=========================================================================

### Masalah:
* Watermark, Walaupun watermark dihapus setengah.
  Sistem tetap dapat membaca dan mendeteksi dengan kesamaan dari setengah bagian watermark yang ada.

* Logo, Sama halnya watermark.
  Logo BI di buat lebih miring namun latar tetap, sistem tetap dapat membaca.
  
=========================================================================

Jalankan dari file Main.py
untuk nilai pecahan bisa di ubah nilainya disini:

![gambar](https://user-images.githubusercontent.com/101382309/168055383-f7487eed-6104-4c64-a6a6-6a001c86292f.png)

Bagian ini guna memilih file yang akan digunakan ori atau palsu (merupakan nama depan dari file **fk1- fk2- ori-**)

![gambar](https://user-images.githubusercontent.com/101382309/168055473-3b8bc185-ad34-427f-8c00-74503bbe2781.png)


Nilai yang di input diatas akan ditampung disini, untuk memanggil file dengan nilai tersebut.

![gambar](https://user-images.githubusercontent.com/101382309/168055735-156ce940-44ff-4c53-8d94-d1b2ebb74484.png)

Bagian ini untuk menjalankan atau mengeksekusi fungsi 
WM_Detection() pada file WaterMarkDetection.py & Logo_Detection() pada file LogoDetection.py

![gambar](https://user-images.githubusercontent.com/101382309/167837802-104743a8-78ed-41f3-b315-9442ba2b0460.png)

### Submission Files

File berikut disertakan sebagai bagian dari pengiriman:
* Template
* Test
* __pycache__
* LogoDetection.py
* Main.py
* WaterMarkDetection.py
* imutils.py 
