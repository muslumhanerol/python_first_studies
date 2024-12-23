mesaj = "BTK Akademi, Python Kursu"

sonuc= mesaj.upper() #Tüm karakterleri büyük harfe çevirir.
sonuc= mesaj.lower() #Tüm karakterleri küçük harfe çevirir.
sonuc= mesaj.title() #Metindeki kelimelerin sadece baş harflerini büyük yapar.
sonuc= mesaj.capitalize() #Metinin sadece baş harfini büyük harfe çevirir.

sonuc= "abc".isupper() #Büyük harfmi diye sorduk True yada False sonucu verir.
sonuc= "abc".islower() #Küçük harfmi diye sorduk True yada False sonucu verir.

sonuc= mesaj.strip() #Yanlışlık ilestring ifadenin başında yada sonuca boşluk konulmuş ise boşlukları siler.

sonuc= mesaj.split() #Boşluklardan ayırarak metnin liste olarak yazdırır. 'BTK', 'Akademi', 'Pythonn', 'Kursu'
sonuc= mesaj.split(",") #Virgülden ayırarak metnin liste olarak yazdırır. 'BTK Akademi', ' Pythonn Kursu'

sonuc=mesaj.index("Akademi") #Akademi kelimesi sitring ifade içerisinde hangi indexten başlıyor. Sonuç= 4

sonuc=mesaj.startswith("B") #String ifade B ilemi başlıyor sorusu sorar, True döner.
sonuc=mesaj.startswith("a") #String ifade a ilemi başlıyor sorusu sorar, False döner.

sonuc=mesaj.endswith("u") #String ifade u ilemi bitiyor sorusu sorar, True döner.
sonuc=mesaj.endswith("s") #String ifade s ilemi bitiyor sorusu sorar, False döner.

sonuc=mesaj.replace("Python","Javascript") #Strin içerisinde Python kelimesini bul bunun yerine Javascript ifadesini ekle.

print(sonuc)