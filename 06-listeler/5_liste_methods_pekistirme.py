customers = ["sadikturan", "ahmetyşlmaz", "cinarturan", "yigitbilgi"]
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
sonuc = f"{customers[0]} ' isimli müşterinin sipariş toplamı {order_totals[0]} liradır" 

# ikinci dizi elemanı ve fiyat bilgisi aynı şeyler geçerli.
sonuc = f"{customers[1]} ' isimli müşterinin sipariş toplamı {order_totals[1]} liradır" 


#-----------------------------------------------------------------------------------------------------


# 4- Müşterileri alfabetik olarak sıralayınız.
#-----------------------------------------------------------------------------------------------------


# 5- Sipariş toplamlarını azalan şekilde sıralayınız.
#-----------------------------------------------------------------------------------------------------


# 6- En düşük sipariş hangisidir?
#-----------------------------------------------------------------------------------------------------


# 7- "sadikturan" isimli kullanıcının kaç tane siparişi vardır?
#-----------------------------------------------------------------------------------------------------


# 8- Customers listesinden "ahmetyılmaz" isimli kullanıcıyı siliniz.
#-----------------------------------------------------------------------------------------------------


# 9- Listelerdeki tüm içerikleri siliniz.
#-----------------------------------------------------------------------------------------------------


# 10- Kullanıcıdan aldığınız kullanıcı adı ve sipariş toplamlarını listeye ekleyiniz.

print(sonuc)