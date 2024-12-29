# Dictionary Metotları

yemekTarifi ={
    "yemekAdi": "Musakka",
    "yemekTarifi": "Tarif açıklaması",
    "resim": "1.jpg"
}

# access items
sonuc = yemekTarifi["yemekAdi"] # Sonuç=Musakka
sonuc = yemekTarifi.get("yemekAdi") # Key bilgisi parantez içine yazılır ve sonuç getirilie. Sonuç=Musakka
sonuc = yemekTarifi.keys() #Key bilgileri liste olarak gelir. ['yemekAdi', 'yemekTarifi', 'resim']
sonuc = yemekTarifi.values() # Value bilgileri liste olarak gelecek. ['Musakka', 'Tarif açıklaması', '1.jpg']
sonuc = yemekTarifi.items() # Dictionary yapısı listeye çevrilir. [('yemekAdi', 'Musakka'), ('yemekTarifi', 'Tarif açıklaması'), ('resim', '1.jpg')]


# update items
#yemekTarifi["yemekAdi"] = "Mantı" # güncelleme-ekleme işlemi yapar.

#yemekTarifi.update({"yemekAdi":"Mantı"}) # Başka bir güncelleme-ekleme metodu.
#yemekAdi key bilgisi aynı kalırsa güncelleme işlemi yapar, ancak yemekAdi2 dersek ekleme işlemi yapmış olur.
#sonuc = yemekTarifi


# delete items

#yemekTarifi.pop("yemekAdi") # Yemek adı key bilgisi silindi. Çıktı:{'yemekTarifi': 'Tarif açıklaması', 'resim': '1.jpg'}

#yemekTarifi.popitem() # Son eklenen elemanı siler. Sonuç: {'yemekAdi': 'Musakka', 'yemekTarifi': 'Tarif açıklaması'}

yemekTarifi.clear() #Liste içerisindeki bütün elemanları siler.

sonuc=yemekTarifi



print(sonuc)