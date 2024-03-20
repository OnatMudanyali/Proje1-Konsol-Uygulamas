import random
def ytmenü():
    print("╔═════════════════════╗")
    print("║    Yazı_Tura Şans   ║")
    print("║                     ║")
    print("║  1-?                ║")
    print("║  2-?                ║")
    print("║  3-Ana Menü         ║")
    print("║                     ║")
    print("║                     ║")  
    print("║                     ║")
    print("║    Seçimiz nedir?   ║")
    print("╚═════════════════════╝")
    print()
    secim=input("Yapmak istediğiniz işlemin başındaki sayıyı yazınız:")

    if secim=="1":
        print("Yazı geldi...")
        yazi_tura = random.randint(1, 2)
    elif secim=="2":
        print("Tura geldi...")
        yazi_tura = random.randint(1, 2)
        ytmenü()
    elif secim=="3":
         print("Ana Menü'ye dönülüyor.")
         return
    else:
         print("Lütfen menüde bulunan geçerli bir sayı giriniz.")
         ytmenü()
