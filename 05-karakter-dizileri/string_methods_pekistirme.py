kursAdi = "BTK Akademi Python, ile programlama dersleri"
website = "https://www.btkakademi.gov.tr/"

# 1- " BTK Akademi " karakter dizisinin baş ve sondaki boşluk karakterlerini siliniz.
sonuc=" BTK Akademi ".strip()

#---------------------------------------------------------------------------------------

# 2- kursAdi değişkenindeki tüm karakterleri küçük harfe çeviriniz.
sonuc=kursAdi.lower()

#---------------------------------------------------------------------------------------

# 3- website değişkeninde kaç yane "." karakteri vardır?
sonuc=website.count(".")

#---------------------------------------------------------------------------------------
# 4- website değişkeni "https" ile mi başlıyor?
sonuc=website.startswith("https")

#---------------------------------------------------------------------------------------

# 5- website "tr ile mi bitiyor"?
sonuc=website.endswith("tr")

#---------------------------------------------------------------------------------------

# 6- kursAdi içerisindeki tüm karakterler harflerden mi oluşuyor?
sonuc=kursAdi.isalpha() # Sonuç=False çünkü boşluklar var.

#---------------------------------------------------------------------------------------

# 7- kursAdi değişkenindeki tüm boşlukları "-" ile değiştiriniz.
sonuc=kursAdi.replace(" ","-").replace("ç","c").replace("ı","i").replace("ş","s").lower()

#---------------------------------------------------------------------------------------

# 8- kursAdi değişkenindeki Python kelimesinin ReactJs ile değiştiriniz.
sonuc=kursAdi.replace("Python","ReactJs")

#---------------------------------------------------------------------------------------

# 9- website değişkeni "www" içeriyor mu?
sonuc=website.find("www") #index numarasını verir. Eğer birkarakter bulamazsa -1 değerini gönderir.
sonuc=website.index("www") #index numarasını verir. Eğer birkarakter bulamazsa hata değerini gönderir.

#---------------------------------------------------------------------------------------

# 10- kursAdi değişkenini listeye çeviriniz.

sonuc=kursAdi.split(" ") #Boşluklardan ayırarak liste oluşturur.
print(sonuc[2]) #Sonuç içerisindeki 2. index numarasını yazdır.

sonuc=kursAdi.split(",") #Virgülden ayırarak liste oluşturur.



print(sonuc)