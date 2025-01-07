# 1- Yaşı 18' den büyük ya da  veli izni varsa bir işte çalışabilir durumunu kontrol ediniz.

veli_izni = True
yas= 18
sonuc = (veli_izni) or (yas >= 18)

print(sonuc)


# 2- Ders notu 50-100 arasındaysa geçti deilse kalsın bilgisini yazdırınız.
dersNotu = 50
sonuc = (dersNotu >= 50 and dersNotu <= 100)

print(f"ders geçme durumu: {sonuc}")


# 3- Not ortalaması en az 70 puan ve zayıfı yoksa teşekkür belgesi alabilme durumunu kontrol ediniz.

ortalama = 70
zayifSayisi = 0

sonuc = (ortalama >= 70) and (zayifSayisi == 0)

print(sonuc)


# 4- İşe girmek için en az önlisans ya da lisans mezunu olma durumunu kontrol ediniz. Sigara kullanmama koşulu.

egitim = "önlisans"
sigara_icme = False

sonuc = (egitim == "önlisans" or egitim == "lisans") and (not (sigara_icme))

print(sonuc)


# 5- Uygulamaya giriş kontrolünü "username yada email" ve "parola" için yapalım.

email = "akademi@btk.com"
userName = "müslüm"
password = "123456"

girilenBilgi = input("email yada username: ")
girilenParola = input("parola giriniz: ")

sonuc= (email == girilenBilgi or userName == girilenBilgi) and (password == girilenParola)

print(sonuc)