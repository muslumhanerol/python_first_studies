# Numaric
# int= tam sayı veri -- float=ondalıklı veri

# Text
# str= text tabanlı

# Boolen
# bool= koşullu durumları nitelemek


isim= "Ali"
yas= 7
kilo= 15.5
ogranciMi= True

#Verilerin türlerini sorgulama.
print(type(isim))  #str
print(type(yas))   #int
print(type(kilo))  #float
print(type(ogranciMi)) #bool


#print("ad: " + isim + " yas: " + yas + " kilo: " + kilo + " öğrenci mi: " + ogranciMi)
# Yukarıdaki kod çalıştırıldığında tip hatası verir, bu hatayı önlemek için veri dönüşümü yapmalıyız.

print("ad: " + isim + " yas: " + str(yas) + " kilo: " + str(kilo) + " öğrenci mi: " + str(ogranciMi))

