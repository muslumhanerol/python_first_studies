# value types Değer olarak saklanır

# x = 10
# y = 20

# x = y
#y = 30
# print(x, y)

# reference types Değer olarak değil adres olarak saklanır.

a = ["elma","armut"]
b = ["elma","armut"]

a = b # b nin adresi a ya eşitleniyor.

a[0] = "üzüm"

print(a, b) # Her iki listenin 0.indexteki elemanları üzüm olarak değiştirilir.



# liste kopyalama

listeA = [10, 20]
listeB = listeA.copy() # 1.Yöntem listeB ye belleğn farklı bir adresinde bir alan tahsis et ve tahsis edilen alana listeA nın bir kopyasını oluştur demiş olduk.

# listeA üzerinde bir güncelleme yapıldığında listeB üzerinde bu güncelleme görülmez.

listeB = list(listeA) # 2.Yöntem list metodu listeA nın kopyasını listeB ye aktarır, sonuç değişmez.

listeB[0] = 30 #listeB nin 0.index numarası güncellendi nacak bu güncelleme diğer listeye yansımadı.

print(listeA,listeB)