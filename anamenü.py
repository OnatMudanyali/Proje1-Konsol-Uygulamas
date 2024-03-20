print("\033[1;32;40m")
#print("╔"+"═"*20+"╗")
import hesaplamalar.hesapmakinesi
import oyunlar.oyun
import çizimler.çizim
import sağlık.sağlık
import sıcaklık.sıcaklık
import yt.yt
import ülkeler.ülke
import yemekler.yemek
import sporlar.spor
import nothesabı.harfnotu

def anamenu():
    print("╔═════════════════════╗")
    print("║    MUDANYALI APP    ║")
    print("║                     ║")
    print("║  1-Hesap Makinesi   ║")
    print("║  2-Oyunlar          ║")
    print("║  3-Çizimler         ║")
    print("║  4-Sağlık           ║")
    print("║  5-Sıcaklık         ║")
    print("║  6-Yazı-Tura        ║")
    print("║  7-Ülkeler          ║")
    print("║  8-Yemekler         ║")
    print("║  9-Sporlar          ║")
    print("║  10-Not Hesabı      ║")
    print("║                     ║")
    print("║                     ║")
    print("║    Seçimiz nedir?   ║")
    print("╚═════════════════════╝")
    print()
    secim=input("Lütfen seçiminizin başındaki sayıyı yazınız:")
    if secim=="1" :
        hesaplamalar.hesapmakinesi.hmmenü()
        anamenu()
    elif secim=="2" :
        oyunlar.oyun.oyunlarmenü()
        anamenu()
    elif secim=="3":
        çizimler.çizim.çizimmenü()
        anamenu()
    elif secim=="4" :
        sağlık.sağlık.sağlıkmenü()
        anamenu()
    elif secim=="5" :
        sıcaklık.sıcaklık.sıcaklıkmenü()
        anamenu()
    elif secim=="6" :
        yt.yt.ytmenü()
        anamenu()
    elif secim=="7" :
        ülkeler.ülke.ülkemenü()
        anamenu()
    elif secim=="8" :
        yemekler.yemek.yemekmenü()
        anamenu()
    elif secim=="9" :
        sporlar.spor.spormenü()
        anamenu()
    elif secim=="10" :
        nothesabı.harfnotu.harfnotumenü()
        anamenu()
    else:
        print("Lütfen menüde bulunan geçerli bir sayı giriniz.")
        anamenu()

anamenu()    
# 201 ╔
# 205 ═
# 187 ╗
# 186 ║
# 200 ╚
# 188 ╝
