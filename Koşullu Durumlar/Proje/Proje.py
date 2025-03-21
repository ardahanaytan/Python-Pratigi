def gorev1():
    note = int(input("Notunuzu girin: "))

    if note > 100 or note < 0:
        print("Geçersiz Not")
    elif note > 90:
        print("AA")
    elif note > 80:
        print("BA")
    elif note > 70:
        print("BB")
    elif note > 60:
        print("CB")
    elif note > 50:
        print("CC")
    elif note > 40:
        print("DC")
    elif note > 30:
        print("DD")
    else: 
        print("FF")


def gorev2():
    para = 0
    password = int(input("4 haneli şifrenizi girin: "))
    
    if password != 1234:
        print("Şifre Yanlış")
    else:
        while(True):
            tercih = input("Bakiye Görüntülemek için B, Para Yatırma için Y, Para Çekme için C, Çıkış için E girin: ")

            if tercih == 'B':
                print("Bakiyeniz: {0}".format(para))
            elif tercih == 'Y':
                miktar = int(input("Yatırmak istediğiniz miktarı yazın: "))
                para += miktar
            elif tercih == 'C':
                miktar = int(input("Çekmek istediğiniz miktarı yazın: "))
                para -= miktar
            elif tercih == 'E':
                print("Hoşçakalın")
                break


def gorev3():
    ay = int(input("Ay numarasi: "))

    if ay == 1 or ay == 3 or ay == 5 or ay == 7 or ay == 8 or ay == 10 or ay == 12:
        print("31 gün")
    elif ay == 4 or ay == 6 or ay == 9 or ay == 11:
        print("30 gün")
    elif ay == 2:
        yil = int(input("Yıl: "))
        if (yil % 4) == 0:
            print("29 gün")
        else:
            print("28 gün")


gorev3(1)