def sıcaklıkmenü():
    print("╔═══════════════════════════════╗")
    print("║       SICAKLIK ÇEVİRME        ║")
    print("║                               ║")
    print("║ 1- Celsius(°C) Fahrenheit(°F) ║")
    print("║    Çevirici                   ║")
    print("║ 2- Fahrenheit(°F) Celsius(°C) ║")
    print("║    Çevirici                   ║")
    print("║ 3- Celsius(°C) Kelvin (K)     ║")
    print("║    Çevirici                   ║")
    print("║ 4- Kelvin(K) Celsius(°C)      ║")
    print("║    Çevirici                   ║")
    print("║ 5- Ana Menü                   ║")
    print("║                               ║")
    print("║                               ║")
    print("╚═══════════════════════════════╝")
    print()
    secim=input("Lütfen seçiminizin başındaki sayıyı yazınız:")
    if secim=="1":
        Celsius=int(input("Lütfen çevrilecek sayıyı yazınız:"))
        Fahrenheit=(1.8*Celsius)+32
        print(f"{Celsius} Celsius(°C) {Fahrenheit} Fahrenheit(°F) eder.")
        sıcaklıkmenü()
    elif secim=="2":
        Fahrenheit=int(input("Lütfen çevrilecek sayıyı yazınız:"))
        Celsius=(Fahrenheit-32)/1.8
        print(f"{Fahrenheit} Fahrenheit(°F) {Celsius} Celsius(°C) eder.")
        sıcaklıkmenü()
    elif secim=="3":
        Celsius=int(input("Lütfen çevrilecek sayıyı yazınız:"))
        Kelvin=Celsius+273.15
        print(f"{Celsius} Celsius(°C) {Kelvin} Kelvin(K) eder.")
        sıcaklıkmenü()
    elif secim=="4":
        Kelvin=int(input("Lütfen çevrilecek sayıyı yazınız:"))
        Celsius=Kelvin-273.15
        print(f"{Kelvin} Kelvin(K) {Celsius} Celsius(°C) eder.")
        sıcaklıkmenü()
    elif secim=="5":
        print("Ana Menü'ye dönülüyor.")
        return
    else:
        print("Lütfen menüde bulunan geçerli bir sayı giriniz.")
        sıcaklıkmenü()

