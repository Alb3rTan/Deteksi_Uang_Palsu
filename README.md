Project ini dikembangkan dari sumber https://github.com/rizanw/uang-matching.git

Image Procesing Project.
Crazy Rich Team:
* Albert Sutandi
* Handinata
* Robert Carlos
* Maichel Valiant


Deteksi Watermark dan Logo BI, sebagai bagian dari Originalitas Mata Uang Rupiah
Cara kerjanya hanya mencocokan 2 Image yaitu Image Pembanding dengan Image yang di Uji.

Library yang digunakan 
import glob
import cv2 
import numpy as np
import imutils                  #Library yang sudah disediakan didalam project 
import tkinter
from tkinter import messagebox  #Menampilkan Jendela Kotak Pesan dari atribute library tkinter
import Main                     #Library untuk mengambil nilai variable yang ada di file Main.py

***Jika library numpy dan cv2 belum terisntal, bisa cari caranya di google***
Untuk project ini di jalankan dengan aplikasi Anaconda Navigator dengan editor Visual studio Code. 

Terdapat 4 file pithon.
* WaterMarkDetection.py => Untuk melakukan deteksi watermark dari uang kertas Rupiah
* LogoDetection.py => Untuk Melakukan deteksi Logo BI yang ada di Uang kertas Rupiah
* imutils.py => Di file ini berisi beberapa fungsi yang digunakan pada file WaterMarkDetection & file LogoDetection.
* Main.py => File ini merupakan file utama untuk menjalankan seluruh file diatas. 

Terdapat 2 Folder
* Folder Template => Berisikan file image pembanding (Training Image) sebagai image pembanding untuk menyatakan
  uang kertas asli atau tidak.
* Folder Test => Berisikan file image uang kertas yang akan di uji keaslianya.

Setiap pecahan uang Rupiah memiliki watermark dan Latar dari logo Bi yang berbeda,
jadi dapat digunakan untuk melakukan penyesuaian guna mendeteksi originalitas dari uang pecahan tersebut.

============================================================================================================
Sukses:
* Watermark hanya terdeteksi dengan pecahan uang yang sama.
* Logo hanya terdeteksi dengan pecahan uang yang sama.
============================================================================================================
Masalah:
* Watermark, Walaupun watermark dihapus setengah.
  Sistem tetap dapat membaca dan mendeteksi dengan kesamaan dari setengah bagian waermark yang ada.
============================================================================================================
* Logo, Sama halnya watermark.
  Logo BI di buat lebih miring namun latar tetap, sistem tetap dapat membaca.
  
  
Jalankan dari file Main.py
untuk nilai pecahan bisa di ubah nilainya disini:
  ![gambar](https://user-images.githubusercontent.com/101382309/167837247-b082858b-3b00-44a2-9a84-c396a8ebd24e.png)

Nilai yang di input diatas akan ditampung disini, untuk memanggil file dengan nilai tersebut.
![gambar](https://user-images.githubusercontent.com/101382309/167837657-0b717895-d0e2-4e66-93b7-13d6ad883d7b.png)

Bagian ini untuk menjalankan atau mengeksekusi fungsi WM_Detection() pada file WaterMarkDetection.py & Logo_Detection() pada file LogoDetection.py
![gambar](https://user-images.githubusercontent.com/101382309/167837802-104743a8-78ed-41f3-b315-9442ba2b0460.png)


