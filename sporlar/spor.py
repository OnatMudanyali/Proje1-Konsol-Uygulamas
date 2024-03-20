def spormenü():    
    print("╔═════════════════════╗")
    print("║    Sporlar          ║")
    print("║                     ║")
    print("║  1-Basketbol        ║")
    print("║  2-Futbol           ║")
    print("║  3-Voleybol         ║")
    print("║  4-Yüzme            ║")
    print("║  5-Golf             ║")
    print("║  6-Ana Menü         ║")
    print("║    Seçimiz nedir?   ║")
    print("╚═════════════════════╝")
    print()
    secim=input("Yapmak istediğiniz işlemin başındaki sayıyı yazınız:")
    if secim=="1":
         print("Basketbol nasıl oynanır?")
         print()
         print('''Profesyonel basketbolda beşer kişilik iki takım, yerden yüksekliği Avrupa standartlarına göre 3,05 metre olan ve pota adı verilen, yere paralel konumdaki bir çemberden topu geçirerek, rakibinden daha fazla sayı yapmak suretiyle, on ikişer, onar veya sekizer dakikalık dört periyottan oluşan maçı kazanmaya çalışır.''')

         spormenü()
    elif secim=="2":
         print("Futbol nasıl oynanır ?")
         print()
         print('''Futbol, on birer oyuncudan oluşan iki takım arasında, kendine özgü küresel bir topla oynanan takım sporudur. 21. yüzyıl itibarıyla 200'ün üzerinde ülkede 250 milyonu aşkın oyuncu tarafından oynanmakta olup dünyadaki en popüler spordur.''')
         spormenü()

    elif secim=="3":
         print("Voleybol nasıl oynanır?")
         print()
         print('''Voleybol, file ile ikiye bölünmüş bir oyun alanı üzerinde altı kişilik iki takım ile oynanan, voleybol topuna eller ve kollarla vurarak file üzerinden karşı tarafın oyun alanına gönderme ve yere değmesini sağlama esasına dayalı bir takım sporudur.''')
         spormenü()
    elif secim=="4":
         print("Yüzme sporu nedir?")
         print()
         print('''Yüzme, bireyin tüm bedenini kol ve bacak hareketlerinden başka bir unsur kullanmadan su içinden ilerletmesini gerektiren, bireysel veya takımsal düzeyde gerçekleştirilen bir yarış ya da antrenman sporudur. Bu spor, yüzme havuzlarında veya açık suda (ör. deniz ya da göl içinde) icra edilmektedir. Yüzme yarışı Olimpiyat oyunlarındaki en popüler spor türlerinden biridir.''')
         spormenü()
    elif secim=="5":
         print("Golf Nasıl oynanır?")
         print()
         print('''Golf, doğada özel olarak yapılmış bir golf sahası'nda golf sopası ve küçük sert bir golf topu'yla oynanan oyundur. Oyunun amacı, sahanın belirlenmiş 18 parkurunu (çukurunu) golf topuna en az vuruş yaparak tamamlamaktır.[1] Plaj golfü, disk golf, futgolf, kapalı golf, minigolf, park golfü, kar golfü, hızlı golf, kentsel golf gibi golf çeşitleri bulunuyor. ''')
         spormenü()
    elif secim=="6":
         print("Ana Menü'ye dönülüyor.")
         return
    else:
         print("Lütfen menüde bulunan geçerli bir sayı giriniz.")
         spormenü()




