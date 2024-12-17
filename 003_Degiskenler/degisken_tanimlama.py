# 2000 + 2000 * %10

urunAFiyat = 4000
urunBFiyat = 3000
kdvOrani = 0.20

print (urunAFiyat + (urunAFiyat * 0.20))  # ürün A<
print (urunBFiyat + (urunBFiyat * 0.18))  # ürün B


# print (urunAFiyat + (urunAFiyat * kdvOrani))  # ürün A yeni kdv

urunToplami = urunAFiyat+urunBFiyat
print(urunToplami + (urunToplami * kdvOrani))

