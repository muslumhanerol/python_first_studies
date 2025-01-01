a, b, c = 4, 8, (12, 2)

# 1- Kullanıcıdan aldığınız 2 sayısının çarpımı ile a,b,c toplamının farkı nedir?

# sayi1 = int(input("sayi 1: "))
# sayi2 = int(input("sayi 2: "))

# carpim = sayi1 * sayi2
# toplam = a + b + (c[0] + c[1])

# sonuc = carpim - toplam
# print(sonuc)

#--------------------------------------------------------------------------------------
# 2- c' nin b' ye kalansız bölümünü hesaplayınız.

# sonuc = (c[0] + c[1]) // b
# print(sonuc)

#--------------------------------------------------------------------------------------
# 3- (a,b,c) toplamının mod 7' si nedir?

# sonuc = (a + b + (c[0] + c[1])) % 7
# print(sonuc)

#--------------------------------------------------------------------------------------
# 4- b' nin a. kuvvetini hesaplayınız.

sonuc = b ** a # b nin a kadar çarpımı
print(sonuc)

#--------------------------------------------------------------------------------------
# 5- a, *b, c = (2,4,6,8,13) işlemine göre c' nin küpü nedir?

# * operatörü *a old. b=8 c=13 olur diğer sayılar 2,4,6 a değerinin olur.
# * operatörü *b old. a=2 c=13 olur diğer sayılar 4,6,8 b değerinin olur.
# * operatörü *c old. a=2 b=4 olur diğer sayılar 6,8,13 c değerinin olur.

a, *b, c = (2,4,6,8,13)

print(c ** 3) #c = 13

#--------------------------------------------------------------------------------------
# 6- a, b, *c = (2,4,6,8,13) işlemine göre c' nin değerleri toplamı nedir?

a, b, *c = (2,4,6,8,13)

print(c[0] + c[1] + c[2])