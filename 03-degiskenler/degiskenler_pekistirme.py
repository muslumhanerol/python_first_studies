"""
Aşağıdaki müşteri bilgilerinin ve satın aldığı ürün bilgilerini değişkenler içerisinde saklayınız.
Toplam ödenen ücret nedir?
Ödenen miktarın kdv oranı nedir? (%18)

Müslüm H. Erol
05554443322
mslmhanerol@gmail.com
Gaziantep

Satın alınan ürünler

Ürün adı: Kablosus Mouse
Fiyatı: 550 TL

Ürün adı: Kablosus Klavye
Fiyatı: 650 TL

Ürün adı: Dizüstü Bilgisayar
Fiyatı: 55.000

"""


musteri1Adi = "Müslüm"
musteri1Soyad = "Erol"
musteri1Telefon ="05554443322"
musteri1Email = "mslmhanerol@gmail.com"
musreri1Adres = "Gaziantep"


urun1Ad = "Kablosus Mouse"
urun1Fiyat = 550

urun2Ad = "Kablosus Klavye"
urun2Fiyat = 650

urun3Ad = "Dizüstü Bilgisayar"
urun3Fiyat = 55000


toplamOdenenUcret = urun1Fiyat + urun2Fiyat + urun3Fiyat
# print("Toplam Ödenen Tutar: " + toplamOdenenUcret)
# print("Toplam KDV Oranı: " + toplamOdenenUcret * 0.18)
#Bu şekilde çalıştırısak TypeError: can only concatenate str (not "int") to str hatası alırız.
#string değerleri birleştirebilirsin fakat int değeri birleştiremezsin.

print("Toplam Ödenen Tutar: " + str(toplamOdenenUcret)) #sayısal değer str fon. aracılığıyla karakter tabanlı br değere çevrilip toplanması sağlanır.
print("Toplam KDV Oranı: " + str(toplamOdenenUcret * 0.18))
#str nin amacı sayısal değeri string değere çevirir.