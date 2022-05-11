Project ini dikembangkan dari sumber https://github.com/rizanw/uang-matching.git

Image Procesing Project.
Crazy Rich Team:
* Albert Sutandi
* Handinata
* Robert Carlos
* Maichel Valiant

Deteksi Watermark dan Logo BI, sebagai bagian dari Originalitas Mata Uang Rupiah

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
