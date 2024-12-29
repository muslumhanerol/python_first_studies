# Sets

# İndesklemenez. Bellekte az yer kaplar performans artar.
# Sıralanamaz.
# Güncellenemez
# Elemanlar tekrarlanamaz
#Eleman siler ya da ekleriz.
# tuple de () listede [] kullanıyoruz sets de {}.

meyveler={"elma", "armut", "kiraz"}
meyveler2={"elma", "armut", "kiraz","kavun"}


#meyveler={"elma", "armut", "kiraz","kiraz"} # İki kere aynı eleman yazılmaz, tek bir kere ekrana yazdırılır.
#sonuc = meyveler[0] #Hata alınır setlerin indexine erişilemez.

#for x in meyveler: # döngü içinde yazdırma.
#    print(x)

#sonuc = "elma" in meyveler # Herhangi bir eleman listede var mı yokmu sorgular. True yada False değer döner.

meyveler.add("karpuz") #Listeye yeni eleman ekleme.
meyveler.update(meyveler2) # meyveler ve meyveler2 değişkenlerini birleştirdik. Sadece farklı olanlar ekrana yazdırılır, aynı olanlar yazdırılmaz.
meyveler.remove("elma") # Liste üzerinden silme işlemi yapar. Geriye varsa hata döndürür.
meyveler.discard("armut") # Liste üzerinden silme işlemi yapar. Geriye hata döndürmez.

sonuc=meyveler


print(sonuc)

