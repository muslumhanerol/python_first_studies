"""
Uygulama 1: Yarı çapı verilen bir dairenin alan ve çevresini hesaplayınız.
Alan: πr2
Çevre: 2πr

Uygulama 2: Klavyeden girilen km bilgisini mil cinsinden hesaplayınız.
mil = km / 1.609344

"""

# Uygulama 1
# pi= 3.14
# r= float(input("Yarı Çap: "))

# alan = pi * (r ** 2) # r * r = r ** 2 demek. r ** 2= r nin karesi
# cevre = 2 * pi * r 

# print("Alan: " + str(alan))
# print("Çevre: " + str(cevre))


#Uygulama2
mesafeKm= input("km: ")
mesafeMil= float(mesafeKm) / 1.609344
mesafeMil = round(mesafeMil,2) # Hesaplanan bilgi yuvarlandı, virgülden sonra 2 sayı yazılacak.
print(mesafeKm + "km= " + str(mesafeMil) + "mil")
