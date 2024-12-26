customers = ["sadikturan", "ahmetyilmaz", "cinarturan", "yigitbilgi"]
order_totals = [12000, 13000, 5000, 15000]

# 1- "sadikturan" kullanıcı adıyla yapılan 5000 liralık sipariş listeye ekleyiniz.
customers.append("sadikturan")
order_totals.append(5000)

# sonuc=customers
# sonuc=order_totals

#-----------------------------------------------------------------------------------------------------

# 2- Son eklenen siparişi siliniz.
# customers.pop() #pop eklenen son elemanı siler.
# order_totals.pop()

# sonuc=customers
# sonuc=order_totals

#-----------------------------------------------------------------------------------------------------

# 3- Tüm müşteriler için aşağıdaki özet cümleyi yazdırınız.
    # "<username>" isimli müşterinin sipariş toplamı "<10000>" liradır.

# {customers[0]} = customers dizisi 0. index, yani saıkturan. order_totals[0] = order_totals dizisi 0.index yani 12000.
# sonuc = f"{customers[0]} ' isimli müşterinin sipariş toplamı {order_totals[0]} liradır" 

# ikinci dizi elemanı ve fiyat bilgisi aynı şeyler geçerli.
# sonuc = f"{customers[1]} ' isimli müşterinin sipariş toplamı {order_totals[1]} liradır" 

#-----------------------------------------------------------------------------------------------------

# 4- Müşterileri alfabetik olarak sıralayınız.

customers.sort() #a dan z ye sıralama yapar.
print(customers)

#-----------------------------------------------------------------------------------------------------

# 5- Sipariş toplamlarını azalan şekilde sıralayınız.

order_totals.sort() # Bu fonk. artan şekilde sıralar.
order_totals.reverse() # Sonucu ters çevirisiz ve azalan şekilde sıralama yapmış olur.

#print(order_totals)

#-----------------------------------------------------------------------------------------------------

# 6- En düşük sipariş hangisidir?

sonuc= min(order_totals) 
sonuc= max(order_totals)

#-----------------------------------------------------------------------------------------------------

# 7- "sadikturan" isimli kullanıcının kaç tane siparişi vardır?

sonuc = customers.count("sadikturan") #append edilenle beraber 2.

#-----------------------------------------------------------------------------------------------------

# 8- Customers listesinden "ahmetyılmaz" isimli kullanıcıyı siliniz.

customers.remove("ahmetyilmaz")
#sonuc=customers

#-----------------------------------------------------------------------------------------------------

# 9- Listelerdeki tüm içerikleri siliniz.

# customers.clear() 
# order_totals.clear()

# sonuc=customers
# sonuc=order_totals

#-----------------------------------------------------------------------------------------------------

# 10- Kullanıcıdan aldığınız kullanıcı adı ve sipariş toplamlarını listeye ekleyiniz.

userName = input("müşteri adı: ")
toplam= input("toplam: ")

customers.append(userName)
order_totals.append(toplam)


print(customers)
print(order_totals)
