#Yapılacaklar listesi
yapilacaklar=[]
print("---Yapilacaklar Listesi---")

while True:
    print("\n1.Listeyi Görüntüle")
    print("2.Madde Ekle")
    print("3.Madde Sil")
    print("4.Çıkış")

    secim=input("\nBir seçenek seç (1/2/3/4):")

    if secim=="1":
        print("\n---YAPILACACAKLAR LİSTEN---")
        if not yapilacaklar:
            print("Liste şu an boş!")
        else:
            for gorev in yapilacaklar:
             print("-"+gorev)

    elif secim=="2":
        yeni_gorev=input("Ne eklemek istersin?")
        yapilacaklar.append(yeni_gorev)
        print("Eklendi!")

    elif secim=="3":
        silinecek=input("Silmek istediğin maddenin adını yaz:")
        if silinecek in yapilacaklar:
            yapilacaklar.remove(silinecek)
            print("Başarıyla silindi.")

    elif secim=="4":
        print("Göürüşürüzz<3")
        break

    else:
        print:("Geçersiz bir sayı girdin, lütfen tekrar dene.")
