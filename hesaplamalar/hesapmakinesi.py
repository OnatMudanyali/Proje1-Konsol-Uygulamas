#print("╔"+"═"*20+"╗")
def hmmenü():
    print("╔═════════════════════╗")
    print("║    Hesap Makinesi   ║")
    print("║                     ║")
    print("║  1-Toplama          ║")
    print("║  2-Çıkarma          ║")
    print("║  3-Çarpma           ║")
    print("║  4-Bölme            ║") 
    print("║  5-Üst Alma         ║")
    print("║  6-Ana Menü         ║")
    print("║                     ║")
    print("║                     ║")
    print("║    Seçimiz nedir?   ║")
    print("╚═════════════════════╝")
    print()
    secim=input("Yapmak istediğiniz işlemin başındaki sayıyı yazınız:")
    if secim=="1":
        sayi1=int(input("Lütfen 1. sayıyı giriniz."))
        sayi2=int(input("Lütfen 2. sayıyı giriniz."))
        print("Sonuç:",sayi1+sayi2)
        hmmenü()
    elif secim=="2":
        sayi1=int(input("Lütfen 1. sayıyı giriniz."))
        sayi2=int(input("Lütfen 2. sayıyı giriniz."))
        print("Sonuç:",sayi1-sayi2)
        hmmenü()
    elif secim=="3":
        sayi1=int(input("Lütfen 1. sayıyı giriniz."))
        sayi2=int(input("Lütfen 2. sayıyı giriniz."))
        print("Sonuç:",sayi1*sayi2)
        hmmenü()
    elif secim=="4":
        sayi1=int(input("Lütfen 1. sayıyı giriniz."))
        sayi2=int(input("Lütfen 2. sayıyı giriniz."))
        print("Sonuç:",sayi1/sayi2)
        hmmenü()
    elif secim=="5":
        sayi1=int(input("Lütfen 1. sayıyı giriniz."))
        sayi2=int(input("Lütfen 2. sayıyı giriniz."))
        print("Sonuç:",sayi1**sayi2)
        hmmenü()
    elif secim=="6":
        print("Ana Menü'ye dönülüyor.")
        return
    else:
        print("Lütfen menüde bulunan geçerli bir sayı giriniz.")
        hmmenü()

