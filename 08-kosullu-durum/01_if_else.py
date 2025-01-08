#parantez içi doğru değer ürettiği sürece çıktı alınır.

# sonuc = 3 > 2

# if (sonuc):
#     print("Merhaba") # Ekrana Merhaba yazar.



# sonuc = 3 > 7

# if (sonuc):
#     print("Merhaba") # Ekrana Merhaba yazmaz.

#-----------------------------------------------------------------

# email = "akademi@btk.com"
# parola = "123456"

# login = (email == "akademi@btk.com") and (parola == "123456")

# if(login):
#     print("Login olundu.")
# else:
#     print("email yada parola yanlış.")

#-----------------------------------------------------------------
# not operatörlü kullanım.

# email = "akademi@btk.com"
# parola = "12345"

# login = (email == "akademi@btk.com") and (parola == "12345")

# if(not(login)): # not = tam tersi soru sorar. login false cevabını getirirse tam tersi cevap verir.
#     print("email yada parola yanlış.")
# else:
#     print("Login olundu.")   
    
    

#-----------------------------------------------------------------

# Hangi parametrenin doğru ve yanlış olduğu ayrımını yapma.

email = "akademi@btk.com"
parola = "123456"



if(email == "akademi@btk.com"):
    if(parola == "123456"):
        print("Login olundu.")
    else:
        print("Parola yanlış")    
else:
    print("email yanlış.") 