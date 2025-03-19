import math

#1. Liste İşlemleri
urun_fiyatlari = [120, 250, 300, 150, 700, 450, 200, 90, 400, 600]

def fiyatlarin_min_max(urunler):
    return max(urunler), min(urunler)

def fiyat_ortalamasi(urunler):
    return sum(urunler)/len(urunler)

def ucyuz_ustu(urunler):
    sonuc = []
    for i in urunler:
        if i > 300:
            sonuc.append(i)
    return sonuc

#2. Sözlük (Dictionary) İşlemleri

def ikinci_islem():
    siparisler = {
        "Ali": [300, 150, 700],
        "Ayşe": [200, 90],
        "Mehmet": [120, 250, 400],
        "Zeynep": [600, 450, 300]
    }

    siparisler_toplam = dict()

    for i in siparisler.keys():
        siparisler_toplam[i] = sum(siparisler[i])

    print(siparisler_toplam)
    print(max(siparisler_toplam))
    liste = []
    for i in siparisler_toplam:
        if siparisler_toplam[i] > 500:
            liste.append(i)
    print(liste)


#3. Karakter Dizileri (String) İşlemleri

def ucuncu_islem():
    ad = input("İsminizi girin: ")
    soyad = input('Soyisminizi girin: ')
    yas = int(input("Yaşınızı girin: "))

    print("Ad: {0}\nSoyad: {1}\nYaş: {2}\nYaşınızın 5 yıl sonraki hali: {3}".format(ad, soyad, yas, yas + 5))


#4. Ekstra Zorluk (Opsiyonel)

def dorduncu_islem():
    girdi = "Python çok güçlü bir programlama dili ve Python öğrenmesi eğlencelidir."

    kelimeler = dict()

    for kelime in girdi.split():
        if kelime not in kelimeler.keys():
            kelimeler[kelime] = 1
        else:
            kelimeler[kelime] += 1

    print(kelimeler)