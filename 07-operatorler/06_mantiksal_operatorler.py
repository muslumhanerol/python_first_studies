# (yas >= 10) => true, false
# (mezuniyet == "lise") ya da (mezuniyet == "üniversite") => true, false

#sonuc = (yas >= 18) ve (mezuniyet == "lise") ve ya mezuniyet == "üniversite")


#1- and = her iki koşul da sağlamalı.

# True, True => True
# True, False => False
# False, False => False

# x = 9

# sonuc = (x > 5) and (x < 10)

# print(sonuc)

#-------------------------------------------------------------------------------------------

#2- or = iki koşuldan birinin sağlanması sonucu True döner.

# True, True => True
# True, False => True
# False, False => False

# x = 10

# sonuc = (x > 5) and (x % 2 == 0) # x pozitif çift sayı ise sonuç True
# sonuc = (x > 5) and (x % 2 == 0) # x pozitif ya da çift ise sonuç True


# print(sonuc)

#-------------------------------------------------------------------------------------------

#3- not = True ise False, False ise True cevabı döner.

x = 11

sonuc = not(x > 0) # Çıktı normalde True fakat not old. çıktı False dır.


print(sonuc)