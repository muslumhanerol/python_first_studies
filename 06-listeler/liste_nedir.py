#split()= string ifadeyi diziye dönüştürür.


kurum = "BTK AKADEMİ".split()

print(type(kurum))
print(kurum)
print(kurum[0]) #Dizinin birinci elemanını yazdır.
print(kurum[1]) #Dizinin ikinci elemanını yazdır.


sayilar= [1,2,3,4,5]
isimler=["ali","ahmet","ayşe"]


print(type(sayilar)) #Değişkenin tipi Liste
print(type(sayilar[0])) #Listedeki ilk elemanın tipi int

print(type(isimler)) #Değişkenin tipi Liste
print(type(isimler[0])) #Listedeki ilk elemanın tipi str


ogrenci=["Çınar","Turan",60,50,70]

print(ogrenci[0] + " " + ogrenci[1])