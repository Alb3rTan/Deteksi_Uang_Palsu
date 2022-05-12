import WaterMarkDetection
import LogoDetection

Input_nilai = "2" # Ubah nilai disini kelipatan seribu (2=2k, 5=5k, 10=10k, 20=20k)
orifake = "3" # ubah nilai disini untuk mengganti file ori atau palsu tipe satu dan palsu tipe dua. (1, 2, 3)

#kondisional untuk nama file yang akan dipanggil
if (orifake == '1'):
    orifakedata = "ori-"
elif(orifake == '2'):
    orifakedata = "fk1-"
elif(orifake == '3'):
    orifakedata = "fk2-"
                      
   
# Variable untuk menampung nilai Input, yang akan digunakan untuk WaterMarkDetection & LogoDetection
Tamplate_wm = "wm-"+Input_nilai+"k.jpg"
Tamplate_lg = "lg-"+Input_nilai+"k.jpg"
Image = orifakedata+Input_nilai+"k.jpg"

# Fungsi Utama untuk menjalankan fungsi WaterMarkDetection & LogoDetection
def Main_Detection():
    WaterMarkDetection.WM_Detection()
    LogoDetection.Logo_Detection()

# Untuk menjalankan Fungsi Mai_Detection()
if __name__ == "__main__": 
    Main_Detection()

#Sukses:
#Watermark hanya terdeteksi dengan pecahan uang yang sama
#Logo hanya terdeteksi dengan pecahan uang yang sama
#

#Masalah:
#Watermark, Walaupun watermark dihapus setengah. sistem tetap dapat membaca dan mendeteksi dengan kesamaan dari setengah bagian waermark yang ada.
#Logo, Sama halnya watermark. Logo BI di buat lebih miring namun latar tetap, sistem tetap dapat membaca. 
 
