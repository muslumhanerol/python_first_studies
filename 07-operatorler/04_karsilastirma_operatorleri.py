a, b, c, d = 2, 2, 10, 5

eposta = "info@btkakademi.com"
parola = "135790"

sonuc = (a == b) # True
sonuc = (a == c) # False
sonuc = (a != c) # True
sonuc = (a != a) #False

# sonuc = (eposta == input("eposta: ")) #eposta adresi doğru yazılırsa True, yanlış yazılırsa False
# sonuc = (parola == input("parola: "))

sonuc = (a > b) # False
sonuc = (c > a) # True

sonuc = (a >= a) # Büyük yada eşit mi True
sonuc = (a < a)  # False
sonuc = (a <= a) # Küçük yada eşit mi True

sonuc = (True == 1) # True
sonuc = (False == 0) # True

sonuc = int(True) #Çıktı 1
sonuc = int(False) #Çıktı 0


print(sonuc)