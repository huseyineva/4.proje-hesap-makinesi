import time

baslik = "Bu bir hesap makinesidir."
giris="""
(1) = Toplama işlemi
(2) = Çıkarma işlemi
(3) = Çarpma işlemi
(4) = Bölme işlemi 
(5) = Karesini bulma işlemi
(6) = Karakökünü bulma işlemi
Çıkış için bu sayılardan farklı bir sayıya basmanız yeterlidir.
"""
islemler = {
    "1":"Toplama-Toplanacak değerin ilkini giriniz: ",
    "11":"Toplanacak değerin ikincisini giriniz: ",
    "2":"Çıkarma-Çıkarılacak değerin ilkini giriniz: ",
    "22":"Çıkarılacak değerin ikincisini giriniz: ",
    "3":"Çarpma-Çarpılacak değerin ilkini giriniz: ",
    "33":"Çarpılacak değerin ikincisini giriniz: ",
    "4":"Bölme-Bölünecek değerin ilkini giriniz: ",
    "44":"Bölünecek değerin ikincisini giriniz: ",
    "5":"Karesini Bulma-Karesi bulunacak değeri giriniz: ",
    "6":"Karakök-Karakökü bulunacak değeri giriniz: "
}

print(baslik, giris, sep="\n")


while True:

    islem = input("Yapmak istediğiniz işlemin numarasını giriniz: ")

    try:
        if islem in ["1", "2", "3", "4", "5", "6"]:
            sayi1 = int(input("{}".format(islemler[islem].split("-")[1])))
            if (islem+islem) in islemler:
                sayi2 = int(input("{}".format(islemler.get(islem+islem))))

    except:
            print("Bir tam sayı girilmedi. Lütfen tekrar deneyiniz!")
            continue

    if islem == "1":
        sonuc = sayi1 + sayi2
    elif islem == "2":
        sonuc = sayi1 - sayi2
    elif islem == "3":
        sonuc = sayi1 * sayi2
    elif islem == "4":
        sonuc = sayi1 / sayi2
    elif islem == "5":
        sonuc = sayi1**2
    elif islem == "6":
        sonuc = sayi1**0.5

    else:
        print("Doğru bir işlem numarası girmediniz. Sistem kapatılıyor!")
        time.sleep(5)
        break

    print("{} işleminin sonucu olarak {} değeri bulunmuştur.\n".format(islemler[islem].split("-")[0], sonuc))
