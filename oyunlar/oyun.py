def oyunlarmenü():
    print("╔═════════════════════╗")
    print("║    Oyunlar          ║")
    print("║                     ║")
    print("║  1-Efootball        ║")
    print("║  2-Fc 24            ║")
    print("║  3-CSGO             ║")
    print("║  4-sims             ║")
    print("║  5-League of Legends║")  
    print("║  6-Ana Menü         ║")  
    print("║                     ║")
    print("║    Seçimiz nedir?   ║")
    print("╚═════════════════════╝")
    print()
    secim=input("Yapmak istediğiniz işlemin başındaki sayıyı yazınız:")
    if secim=="1":
         print("Efootball oyunu nedir?")
         print()
         print('''eFootball, Konami Digital Entertainment tarafından geliştirilen ve Konami tarafından yayınlanan 30 Eylül 2021'de yayınlanmış bir futbol simülasyonu video oyunudur. Orijinal Pro Evolution Soccer (Japonya'da Winning Eleven olarak bilinir) serisinden eFootball serisine tamamen yeniden markalaştırıldıktan sonra oynaması ücretsiz bir oyun olmuştur.''')

         oyunlarmenü()
    elif secim=="2":
         print("Fc 24 oyunu nedir?")
         print()
         print('''EA Sports FC 24[1] yeni bir futbol video oyunudur. EA Vancouver ve EA Romania tarafından geliştirildi ve EA Sports tarafından yayınlandı. EA'nın FIFA ile ortaklığının sona ermesinin ardından EA Sports FC serisinin açılış oyunu olarak EA Sports tarafından geliştirilen oyun, 29 Eylül 2023 tarihinde Nintendo Switch, PlayStation 4, PlayStation 5, Windows, Xbox One ve Xbox Series X/S için dünya çapında piyasaya sürülmüştür. Oyunda bir önceki HyperMotion 2 teknolojisinin bir üst versiyonu HyperMotionV teknolojisi kullanıyor.

    PlayStation 5, Xbox Series X|S ve oyunun bilgisayar sürümleri çapraz platform aracılığıyla oynanabilecektir. PlayStation 4 ve Xbox One sürümlerinin çapraz platformda oynanabilecek. Oyunun Nintendo Switch sürümü ise çapraz platform desteklememektedir.

    Oyunun tanıtım filminde FIFA 14'de kullanılan müziklerden birisi olan Love Me Again kullanıldı.''')
         oyunlarmenü()

    elif secim=="3":
         print("CSGO oyunu nedir?")
         print()
         print('''Counter-Strike: Global Offensive ya da kısa adıyla CS:GO, Valve ve Hidden Path Entertainment tarafından geliştirilen çevrimiçi birinci şahıs nişancı oyunudur. Counter-Strike serisinin dördüncü oyunudur. Ağustos 2012'de Microsoft Windows, macOS, Xbox 360 ve PlayStation 3 için piyasaya sürülürken, Linux sürümü 2014'te piyasaya sürülmüştür.Oyun, teröristler ve anti-Teröristler adlı takımı Her iki taraf da birbirlerini yok etmeleriyle ve aynı zamanda ayrı hedefleri tamamlamakla görevlidir. Teröristler, oyun moduna bağlı olarak ya bombayı yerleştirmeli ya da rehineleri savunmalıdır; anti-teröristler ise ya bombanın yerleştirilmesini önlemeli, bombayı etkisiz hale getirmeli ya da rehineleri kurtarmalıdır.''')
         oyunlarmenü()
    elif secim=="4":
         print("sims oyunu nedir?")
         print()
         print('''The Sims, Maxis tarafından geliştirilen ve Electronic Arts tarafından 2000 yılında yayınlanan stratejik yaşam simülasyonu video oyunudur. "Sim" adı verilen sanal insanların kurgusal bir mahalle içerisinde yaşadığı evlerde bilgisayar simülasyonu üzerinden günlük aktiviteleri kontrol edilir. Oyuncular Sim'leri kontrol edebilir, kariyerlerini geliştirebilir, yaşadıkları alanı değiştirebilir ve diğer Sim'lerle ilişki kurabilirler. Aynı zamanda Sim'ler için ev yaratabilir, evi dekor edebilir, kıyafet alabilirler. Diğer Sim'lerle olan sosyal ilişkilerini de ilerletebilirler.''')
         oyunlarmenü()
    elif secim=="5":
         print("League of Legends oyunu nedir?")
         print()
         print('''League of Legends (kısaca LoL, Türkçe anlamı: Efsaneler Ligi), Riot Games tarafından geliştirilen ve yayımlanan video oyunu.[1] 27 Ekim 2009 tarihinde Riot Games'in ilk oyunu olarak "League of Legends: Clash of Fates" adıyla piyasaya çıkmıştır.[2][3] MOBA türü strateji oyunudur.[1] Oyun Warcraft III haritası olan Defense of the Ancients örnek alınarak yapılmıştır.[4] Oyunun baş tasarımcısı, Defense of the Ancients (DotA) haritasını tasarlayan Steve Feak'dir.''')
         oyunlarmenü()
    elif secim=="6":
         print("Ana Menü'ye dönülüyor.")
         return
    else:
         print("Lütfen menüde bulunan geçerli bir sayı giriniz.")
         oyunlarmenü()
