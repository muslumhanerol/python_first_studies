kurs= "Python ile Programlama"

#print(kurs[0]) # kurs değişkeninin ilk index karakteri gelir, yani P.

#print(kurs[-1]) # kurs değişkeninin SON index karakteri gelir, yani a. -2 olsaydı m.


adet = len(kurs) #Karakter sayısı öğrenme, boşluklar dahil edilir .
print(adet)
print(kurs[adet - 1]) #len fonksiyonu ile karakter sayısını bulur 1 eksiğini alır ve yine istediğimiz karaktere erişebiliriz. Burada a karakterine eriştik.


print(kurs[0:5]) #Belirli bir index alanını alır. Burada 0 dan başlar 0 dahil 5 e kadar alır 5 hariç. Pytho çıktısı elde edilir.
print(kurs[:5]) # Yukarıdakinin bir başka yazım şekli, aynı çıktıyı verir Pytho.

print(kurs[11:22]) #Son karakteri de almak istiyorsak bir fazlasını yaz. Çıktı= Programlama
print(kurs[11:len(kurs)]) # 11. indexten başla kursun sonuna kadar ne varsa al. Yukarıdakinin farklı bir yazımı. Çıktı= Programlama

print(kurs[5:]) #Başlanğıç indexi verilip sonu verilmezse yine sonuna kadar gider. Çıktı= n ile Programlama
print(kurs[11:]) #Çıktı= Programlama
print(kurs[-11:-1]) # Son karakter alınmaz. Çıktı= Programlam


#Seçerek yazdırma. Adım sayısı.
print(kurs[0:20:1]) # 0 dan 20 ye kadar 1 er 1 er al. Çıktı= Python ile Programla
print(kurs[0:20:2]) # 0 dan 20 ye kadar 2 şer 2 şer al. Çıktı= Pto l rgal


print(kurs[::]) # Strigni olduğu gibi alır.
print(kurs[::2]) # Strigni 2 şer 2 şer alır.
print(kurs[::-1]) # Stringi ters çevirir. Çıktı= amalmargorP eli nohtyP



