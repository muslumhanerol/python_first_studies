#Key-value türünde bilgi saklar.
#Sıralanır, Güncellenir, Tekrarlanmaz.

# key - value
# sehirler = ["kocaeli", "istanbul"]
# plakalar = [41,34]

# print(plakalar[0], sehirler[0]) # plakalardaki 0.index sehirlerdeki 0. indexe karşılık gelir.
# print(plakalar[1], sehirler[1])

# print(plakalar[sehirler.index("istanbul")]) #sehirler üzerinden index metodu aracılığla istanbul valuesine sahip olan bilginin indexini bul.
# print(plakalar[sehirler.index("kocaeli")])

#---------------------------------------------------------------------------------------

#dictionary

# İlk yazılan value bilgisi ona karşılık gelen ise değer.
plakalar = {"kocaeli": 41, }