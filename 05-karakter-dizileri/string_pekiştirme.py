title="Python ile programlama dersleri"

# 1- "title" değişken içerisindeki karakter sayısı nedir?

# adet= len(title)
# print(adet)

#-----------------------------------------------------

# 2- "title" içerisindeki "Python" kelimesini alın.

#print(title[:6])

#-----------------------------------------------------

# 3- "title" değişkeninin ilk 5 ve son 5 karakterini alın.

print(title[:6])
print(title[-8:])

#-----------------------------------------------------

# 4- "title" değişkenini tersten yazdırınız.

print(title[::-1]) #Eğer 1 yazsaydık normal yazdıracaktı.

#-----------------------------------------------------

# 5- Klavyeden girilen öğrenci bilgisine göre örnek verilen cümleyi yazdırınız.
#   Örnek: Çınar Turan isimli öğrencinin 1.notu 60, 2.notu 60 ve ortalaması 60 olarak hesaplanmıştır.

ad=input("Adı: ")
soyad=input("Soyad: ")
not1=input("1.Not: ")
not2=input("2.Not: ")
ortalama= (float(not1) + float(not2)) /2

sonuc= f"{ad} {soyad} isimli öğrencinin 1.notu {not1}, 2.notu {not2} ve ortalaması {ortalama} olarak hesaplanmıştır."
print(sonuc)