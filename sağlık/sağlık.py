def sağlıkmenü():
    print("╔═════════════════════════════════╗")
    print("║     Sağlık(Kilo Hesaplayıcı)    ║")
    print("║                                 ║")
    print("║  1- Vücut Kitle İndeksi'ne      ║")
    print("║     Göre İdeal Kilo Hesaplama   ║")
    print("║  2- Broca Formülü İle           ║")
    print("║     İdeal Kilo Hesaplama        ║")
    print("║  3- Erkekler İçin               ║")
    print("║     Robinson Formülü İle        ║")
    print("║     İdeal Kilo Hesaplama        ║")
    print("║ 4- Kadınlar İçin                ║")
    print("║     Robinson Formülü İle        ║")
    print("║     İdeal Kilo Hesaplama        ║")
    print("║ 5- Kilo Durumu Değerlendirme    ║")
    print("║ 6- İdeal Kilo Hesaplayarak      ║")
    print("║     Kilo Durumu Değerlendirmesi ║")
    print("║ 7- Ana Menü                     ║")
    print("║           Seçiminiz nedir?      ║")
    print("║                                 ║")
    print("╚═════════════════════════════════╝")
    print()
    secim=input("Lütfen seçiminizin başındaki sayıyı yazınız:")
    if secim=="1":
        kilo=int(input("Lütfen kilonuzu giriniz (KG):"))
        boy=int(input("Lütfen boyunuzu giriniz (CM):"))
        boy2=boy/100
        vki=kilo/(boy2*boy2)
        ik=vki*(boy2*2)
        print(f"Vücut kitle endeksiniz {vki} kg/m2, ideal kilonuz {int(ik)} kg'dır.")
        sağlıkmenü()
    elif secim=="2":
        boy=int(input("Lütfen boyunuzu giriniz (CM):"))
        boy2=boy/100
        ik2=(boy-100)-((boy-150)/4)
        print(f"Broca formülüne göre ideal kilonuz: {int(ik2)}")
        sağlıkmenü()
    elif secim=="3":
        boy=int(input("Lütfen boyunuzu giriniz (CM):"))
        boy2=boy/100
        ik9=boy*0.748-62
        print(f"Erkekler için Robinson formülüne göre ideal kilonuz: {int(ik3)}")
        sağlıkmenü()
    elif secim=="4":
        boy=int(input("Lütfen boyunuzu giriniz (CM):"))
        boy2=boy/100
        ik10=boy*0.67-53
        print(f"Kadınlar için Robinson formülüne göre ideal kilonuz: {int(ik4)}")
        sağlıkmenü()
    elif secim=="5":
        kilo=int(input("Lütfen kilonuzu giriniz (KG):"))
        boy=int(input("Lütfen boyunuzu giriniz (CM):"))

        boy2=boy/100
        vki=kilo/(boy2*boy2)
        ik=vki*(boy2*2)

        if kilo>ik:
            print("Vücut kitle endeksine göre kilonuz", int(kilo - ik), "kg fazla.")
        elif kilo<ik:
            print("Vücut kitle endeksine göre kilonuz", int(ik - kilo), "kg az.")
        else:
            print("Vücut kitle endeksine göre kilonuz tam yerinde.")
        
        boy2=boy/100
        ik2=(boy-100)-((boy-150)/4)

        if kilo>ik2:
            print("Broca formülüne göre kilonuz", int(kilo - ik2), "kg fazla.")
        elif kilo<ik2:
            print("Broca formülüne göre kilonuz", int(ik2 - kilo), "kg az.")
        else:
            print("Broca formülüne göre kilonuz tam yerinde.")
        
        boy2=boy/100
        ik3=boy*1.063-114

        if kilo>ik3:
            print("Erkekler için Robinson formülüne göre kilonuz", int(kilo - ik3), "kg fazla.")
        elif kilo<ik3:
            print("Erkekler için Robinson formülüne göre kilonuz", int(ik3 - kilo), "kg az.")
        else:
            print("Erkekler için Robinson formülüne göre kilonuz tam yerinde.")

        boy2=boy/100
        ik10=boy*0.67-53

        if kilo>ik4:
            print("Kadınlar için Robinson formülüne göre kilonuz", int(kilo - ik4), "kg fazla.")
        elif kilo<ik4:
            print("Kadınlar için Robinson formülüne göre kilonuz", int(ik4 - kilo), "kg az.")
        else:
            print("Kadınlar için Robinson formülüne göre kilonuz tam yerinde.")
            sağlıkmenü()
    elif secim=="6":
        kilo=int(input("Lütfen kilonuzu giriniz (KG):"))
        boy=int(input("Lütfen boyunuzu giriniz (CM):"))

        boy2=boy/100
        vki=kilo/(boy2*boy2)
        ik=vki*(boy2*2)

        print(f"Vücut kitle endeksiniz {vki} kg/m2, ideal kilonuz {int(ik)} kg'dır.")

        if kilo>ik:
            print("Vücut kitle endeksine göre kilonuz", int(kilo - ik), "kg fazla.")
        elif kilo<ik:
            print("Vücut kitle endeksine göre kilonuz", int(ik - kilo), "kg az.")
        else:
            print("Vücut kitle endeksine göre kilonuz tam yerinde.")
        
        boy2=boy/100
        ik2=(boy-100)-((boy-150)/4)

        print(f"Broca formülüne göre ideal kilonuz: {int(ik2)}")

        if kilo>ik2:
            print("Broca formülüne göre kilonuz", int(kilo - ik2), "kg fazla.")
        elif kilo<ik2:
            print("Broca formülüne göre kilonuz", int(ik2 - kilo), "kg az.")
        else:
            print("Broca formülüne göre kilonuz tam yerinde.")
        
        boy2=boy/100
        ik3=boy*1.063-114

        print(f"Erkekler için Robinson formülüne göre ideal kilonuz: {int(ik3)}")

        if kilo>ik:
            print("Erkekler için Robinson formülüne göre kilonuz", int(kilo - ik), "kg fazla.")
        elif kilo<ik:
            print("Erkekler için Robinson formülüne göre kilonuz", int(ik - kilo), "kg az.")
        else:
            print("Erkekler için Robinson formülüne göre kilonuz tam yerinde.")

        boy2=boy/100
        ik10=boy*0.67-53

        print(f"Kadınlar için Robinson formülüne göre ideal kilonuz: {int(ik10)}")

        if kilo>ik:
            print("Kadınlar için Robinson formülüne göre kilonuz", int(kilo - ik), "kg fazla.")
        elif kilo<ik:
            print("Kadınlar için Robinson formülüne göre kilonuz", int(ik - kilo), "kg az.")
        else:
            print("Kadınlar için Robinson formülüne göre kilonuz tam yerinde.")
            sağlıkmenü()
    elif secim=="7":
        print("Ana Menü'ye dönülüyor.")
        return
   
    else:
        print("Lütfen menüde bulunan geçerli bir sayı giriniz.")
        sağlıkmenü()

 
