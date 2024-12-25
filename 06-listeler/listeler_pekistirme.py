# 1- "Toyota, Bmw, Renault, Mercedes" elemanlarına sahip markalar isimli bir liste oluşturunuz.
markalar=["Toyota","Bmw","Renault","Mercedes"]

#--------------------------------------------------------------------------------------------------

# 2- Liste kaç elemanlıdır?
sonuc = len(markalar)

#--------------------------------------------------------------------------------------------------

# 3- Lşstenşn ilk ve son elemanı nedir?
sonuc = markalar[0]
sonuc = markalar[-1]

#--------------------------------------------------------------------------------------------------

# 4- "Renault" markasını "Togg" ile güncelleyiniz.
markalar[2] = "Togg"
sonuc = markalar

#--------------------------------------------------------------------------------------------------

# 5- "Togg" listenin bir elemanı mıdır?
sonuc ="Togg" in markalar #True
sonuc ="Togg" not in markalar #False

#--------------------------------------------------------------------------------------------------

# 6- Listenin il 2 elemanını alınır.
sonuc = markalar[0:2]

#--------------------------------------------------------------------------------------------------

# 7- Listenin sonuna "Ford" ve "Citroen" markalarını ekleyiniz.
sonuc = markalar + ["Ford","Citroen"]

#--------------------------------------------------------------------------------------------------

# 8- Listenin son elemanını siliniz.
del markalar[-1]
sonuc = markalar

#--------------------------------------------------------------------------------------------------

# 9- Aşağıdaki verileri liste içerisinde saklayınız.

    # Öğrenci1: Yiğit Bilgi 2010 [70,80,90]
    # Öğrenci2: Ada Bilgi 2011 [70,70,80] 
    # Öğrenci3: Çınar Turan 2017 [60,60,90]

ogrenci1=["Yiğit", "Bilgi", 2010,[70,80,90]]
ogrenci2=["Ada", "Bilgi", 2011,[70,70,80]]
ogrenci3=["Çınar", "Turan", 2017,[60,60,90]]

ogrenciler = [ogrenci1,ogrenci2,ogrenci3]

#--------------------------------------------------------------------------------------------------

# 10- Öğrencilerin yaşlarını hesaplayınız.

# yasYigit = 2024 - ogrenci1[2] #Yaş bilgisi 2. indexte.
# yasAda = 2024 - ogrenci2[2]
# yasCınar = 2024 - ogrenci3[2]

#Farklı bir yazım tekniği.
yasYigit = 2024 - ogrenciler[0][2] #[0]=Yiğitin bilgilerinin verir, [2]=Yaş bilgisi 2. indexte.
yasAda = 2024 - ogrenciler[1][2]
yasCınar = 2024 - ogrenciler[2][2]

print(yasYigit,yasAda,yasCınar)

#--------------------------------------------------------------------------------------------------

# 11- Örencilerin not ortalamalarını hesaplayınız.    

#ogrenciler[0][3][0]= [0]=Yiğite karşılık gelir. [3]=Notlar 3. indexte, nota karşılık gelir. [0]=Birinci nota karşılık gelir.
notYigit = (ogrenciler[0][3][0] + ogrenciler[0][3][1] + ogrenciler[0][3][2]) / 3

notAda = (ogrenciler[1][3][0] + ogrenciler[1][3][1] + ogrenciler[1][3][2]) / 3

notCınar = (ogrenciler[2][3][0] + ogrenciler[2][3][1] + ogrenciler[2][3][2]) / 3

print(notYigit,notAda,notCınar)