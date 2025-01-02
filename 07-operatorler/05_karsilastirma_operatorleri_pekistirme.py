# 1- Girilen 2 sayıdan hangisi büyüktür.

# sayi1= int(input("sayı 1: "))
# sayi2= int(input("sayı 2: "))

# sonuc = (sayi1 > sayi2)

# print(f"{sayi1} {sayi2} den büyük mü? {sonuc}")

#-----------------------------------------------------------------------------------
# 2- Girilen bir sayının tek çift kontrolünü yapınız.

# sayi = int(input("sayı: "))

# sonuc = (sayi % 2 == 0) # Sonuç çift ise True değilse False olacak.

# print(f"sayı çift mi?: {sonuc}")

#-----------------------------------------------------------------------------------
# 3- Bir öğrencinin girilen 3 notuna göre başarı durumunu kontrol ediniz. 50 ve üstü başarılı.

not1 = int(input ("Not 1: "))
not2 = int(input ("Not 2: "))
not3 = int(input ("Not 3: "))

ortalama = (not1 + not2 + not3) / 3
                                    
                                    # Sonuç küsüratlı çıkarsa 2 basamaklıya yuvarla.
print(f"Öğrencinin not ortalaması: {round(ortalama, 2)}, Başarı durumu: {ortalama >= 50}")