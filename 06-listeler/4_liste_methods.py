sayilar = [4,6,8,2,56,78,90,4,4]
isimler = ["Ahmet","Canan","Canan","Zeynep","Gökhan","Ali"]

sonuc = min(sayilar) # En küçük sayıyı verir.
sonuc = min(isimler) # Alfabetik olarak ilk harflerden ilklere doğru sıralar.

sonuc = max(sayilar) # En büyük sayıyı verir.
sonuc = max(isimler) # Alfabetik olarak son harflerden ilklere doğru sıralar.

#------------------------------------------------------------------------------------------

#Ekleme

# sayilar.append(12) #En sona ekler
# isimler.append("Çınar") #En sona ekler

# sayilar.insert(0, 100) #Konumlu ekleme, 0. indexe 100 değeri eklenir ve diğer elemanlar sağa kayar.
# sayilar.insert(-1, 100)
# sayilar.insert(-3, 100) #Elemanı sondan bir sağa kaydırır ve eklemeyi yapar.
# sayilar.insert(len(sayilar), 100) # En sona ekleme.

#------------------------------------------------------------------------------------------

#Silme

# sayilar.pop() # Elemanın son index numarası silinir.
# sayilar.pop(0) # Listenin ilk index değerini siler.

# isimler.remove("Canan") # Silinmek istenen eleman bilgisi girilerek silme.

#------------------------------------------------------------------------------------------

#Sıralama

# sayilar.sort() # Sayıların tamanını küçükten büyüğe sıralar.
# isimler.sort() # Alfabenin ilk harfinden sonuna sıralama yapar.
# sayilar.reverse() # Sayıların tamanını büyükten küçüğe sıralar.

#sonuc=sayilar
#sonuc=isimler

#------------------------------------------------------------------------------------------

# Count

# sayilar.sort()
# isimler.sort()
# sayilar.reverse()

# sonuc = sayilar.count(4) # 4 sayısından kaç adet olduğunu göndürür.
# sonuc = isimler.count("Canan") # Canan isminden kaç tane olduğunu göndürür.

#------------------------------------------------------------------------------------------

# Arama

sonuc=sayilar.index(4) #Verilen değerin kaçıncı indexte olduğunu bulur. Burada 0. index
sonuc=sayilar.index(2) #Burada 3. index

print(sonuc)