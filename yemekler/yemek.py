def yemekmenü():    
    print("╔═════════════════════╗")
    print("║    Yemekler         ║")
    print("║                     ║")
    print("║  1-Yemek Ekle       ║")
    print("║  2-Tarhana          ║")
    print("║  3-Mercimek         ║")
    print("║  4-Makarna          ║")
    print("║  5-Mantı            ║")  
    print("║  6-Ana Menü         ║")  
    print("║                     ║")
    print("║    Seçimiz nedir?   ║")
    print("╚═════════════════════╝")
    print()
    secim=input("Yapmak istediğiniz işlemin başındaki sayıyı yazınız:")
    if secim=="1":
     corba1="Tarhana"
    corba2="Mercimek"   
    corbalar =["Tarhana","Mercimek"]
    print(corbalar)
    #corbalar.append(ey)
    corbalar.insert
    yemek1 = "Makarna"
    yemek2 = "Mantı"
    yemekler =[yemek1,yemek2]
    print(yemekler)
    ey = input("Eklenecek yemek nedir?")
    #yemekler.append(ey)
    yemekler.insert(1,ey)

    print("\nÇORBALAR:")
    for a in corbalar:
        print(a)

    print("\nYEMEKLER:")
    for a in yemekler:
        print(a)

    #print(yemekler[-1])
    #print(yemekler[-2]) 

    if secim=="6":
       print("Ana Menü'ye dönülüyor.")
       return
    
