def ülkemenü():    
    print("╔═════════════════════╗")
    print("║    Ülkeler          ║")
    print("║                     ║")
    print("║  1-Türkiye          ║")
    print("║  2-İngiltere        ║")
    print("║  3-Almanya          ║")
    print("║  4-ABD              ║")
    print("║  5-Finlandiya       ║")
    print("║  6-Ana Menü         ║")
    print("║                     ║")
    print("║    Seçimiz nedir?   ║")
    print("╚═════════════════════╝")
    print()
    secim=input("Yapmak istediğiniz işlemin başındaki sayıyı yazınız:")
    if secim=="1":
         print("Türkiye hakkında kısa bilgi verebilir misin?")
         print()
         print('''Türkiye veya resmî adıyla Türkiye Cumhuriyeti, topraklarının büyük bölümü Anadolu'da, diğer bir bölümü ise Balkan Yarımadası'nın güneydoğu uzantısı Trakya'da olan, kıtalararası bir ülkedir Ankara, Türkiye'nin başkenti ve ikinci büyük şehri; İstanbul ise, Türkiye'nin en büyük şehri, ekonomik merkezi ve aynı zamanda Avrupa'nın en büyük şehridir.''')

         ülkemenü()
    elif secim=="2":
         print("İngiltere Hakkında kısa bilgi verebilir misin?")
         print()
         print('''İngiltere (İngilizce: England), Birleşik Krallık'ı meydana getiren dört ülkeden biridir.[6][7][8] Batıda Galler ve kuzeyde İskoçya ile komşudur. Kuzeybatısında İrlanda Denizi, güneybatısında da Kelt Denizi bulunur. Ülkenin doğusunda, kıta Avrupası ile ayrıldığı yerde Kuzey Denizi; güneyinde ise Manş Denizi bulunur. Büyük Britanya'ya ait, Kuzey Atlantik Okyanusu'nda yer alan yaklaşık 100 adet ada İngiltere'ye aittir. Scilly Adaları ve Wight Adası bunlara dahildir.''')
         ülkemenü()

    elif secim=="3":
         print("Almanya hakkında kısa bilgi verebilir misin?")
         print()
         print('''Almanya (Almanca: Deutschland, Almanca telaffuz: [ˈdɔʏtʃlant]) veya resmî ismiyle Almanya Federal Cumhuriyeti (Almanca: Bu ses hakkındaBundesrepublik Deutschland (yardım·bilgi), [ˈbʊndəsʁepuˌbliːk ˈdɔʏtʃlant]), Orta Avrupa'da bulunan bir ülkedir. Kuzeyinde Kuzey Denizi, Danimarka ve Baltık Denizi, doğusunda Polonya ve Çekya, güneyinde Avusturya ve İsviçre, batısında Fransa, Lüksemburg, Belçika ve Hollanda bulunur. Ülke, coğrafi olarak ılıman iklim kuşağında yer alır ve yüzölçümü 357.578 km2dir.''')
         ülkemenü()
    elif secim=="4":
         print("ABD hakkında kısa bilgi verebilir misin?")
         print()
         print('''Amerika Birleşik Devletleri (ABD; İngilizce: United States of America, USA), Birleşik Devletler (BD; İngilizce: United States, US) veya resmî olmayan ismiyle Amerika (İngilizce: America), orta Kuzey Amerika'da, Kanada ve Meksika arasında bulunan,[a] elli eyalet ve bir federal bölgeden oluşan, federal anayasal cumhuriyet ile yönetilen bir ülkedir. Dünya'nın, 9,8 milyon km2 (3,8 milyon sq mi) yüz ölçümü ile karasal alan bakımından dördüncü, toplam alan bakımındansa üçüncü en büyük ülkesi[b] ve 331 milyonu aşan nüfusu ile de en kalabalık üçüncü ülkesidir. Ülkenin başkenti, aynı zamanda federal bölgesi olan Washington, DC'dir. En kalabalık şehri ise New York'tur.''')
         ülkemenü()
    elif secim=="5":
         print("Finlandiya hakkında kısa bilgi verebilir misin?")
         print()
         print('''Finlandiya (Fince: Suomi, İsveççe: Finland) veya resmî adıyla Finlandiya Cumhuriyeti, Kuzey Avrupa'daki bir İskandinav ülkesi. Doğuda Rusya, kuzeyde Norveç ve batıda İsveç'le komşudur. Batıda Botniya ve güneyde Finlandiya körfezlerine kıyısı vardır. Yüz ölçümü 338.455 km² ve nüfusu 5,5 milyondur. Helsinki ülkenin başkenti ve en büyük şehridir. ''')
         ülkemenü()
    elif secim=="6":
         print("Ana Menü'ye dönülüyor.")
         return
    else:
         print("Lütfen menüde bulunan geçerli bir sayı giriniz.")
         ülkemenü()


