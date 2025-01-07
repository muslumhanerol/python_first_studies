#parantez içi doğru değer ürettiği sürece çıktı alınır.

# sonuc = 3 > 2

# if (sonuc):
#     print("Merhaba") # Ekrana Merhaba yazar.



# sonuc = 3 > 7

# if (sonuc):
#     print("Merhaba") # Ekrana Merhaba yazmaz.

#-----------------------------------------------------------------

email = "akademi@btk.com"
parola = "123456"

login = (email == "akademi@btk.com") and (parola == "123456")

if(login):
    print("Login olundu.")
else:
    print("email yada parola yanlış.")