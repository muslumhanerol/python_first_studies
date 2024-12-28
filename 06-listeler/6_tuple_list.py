# elemanları değiştirilemez, silinemez listeler.

my_list = [1,2,3]

my_tuple = (1,2,4,1) #değiştirilemez. #Bir başka yazım tekniği 1,2,3 

# print(type(my_list))
# print(type(my_tuple))

# sonuc=my_list[0] #my_list değişkeni 1.index elemanı. Çıktı= 1
# sonuc=my_tuple[2] #my_tuple değişkeni 2.index elemanı. Çıktı= 4


my_list[0] =2 # 0. indexteki eleman olan 1 i 2 ile değiştirdik. Çıktı=[2, 2, 3]
#my_tuple[0] = 2 # Çıktı= Eleman atama işlemini desteklemiyor.

my_list.append(3) # my_list değişkenine son eleman olarak 3 eklendi.
#my_tuple.append(3) #Bu işlem tuple de yapılamaz, sadece count ve index metodu kullanılır.


sonuc=my_tuple.count(1) # 1 den kaç eleman var çıktısı verir.



print(sonuc)


