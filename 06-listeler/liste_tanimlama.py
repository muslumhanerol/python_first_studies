programlama_dilleri=["Python","C#","Java","Javascript"]

sonuc=programlama_dilleri
sonuc=type(programlama_dilleri)

sonuc=programlama_dilleri[0:2] #0. indexten başlar 2. indexe kadar yazar "Python","C#". 2.indexi yazmaz. 
sonuc=programlama_dilleri[:2] #En soldan başlar 2. indexe kadar yazar "Python","C#". 2.indexi yazmaz.

sonuc=programlama_dilleri[0:] #0. indexten başlar listenin sonuna kadar gider.
sonuc=programlama_dilleri[:] #Listenin başından sonuna kadar gider.

sonuc=programlama_dilleri[-3:-1] #Soldan -3. indexe kadar alır, ancak bitiş indexi dahil olmadığından -1 i almaz.
sonuc=programlama_dilleri[-3:] #-3 den başlar sona kadar alır.


#Güncelleme
programlama_dilleri[-1]="php" #Son elemanın yerine php yazdırdık.


sonuc=programlama_dilleri
sonuc=len(programlama_dilleri) #Dizinin eleman sayısını verir.
sonuc=programlama_dilleri + ["Go","Delphi"] #Diziye yeni eleman ekleme.

sonuc="Python" in programlama_dilleri #Python ifadesi dizi içerisinde var mı? True yada False döner.
sonuc="React" in programlama_dilleri #False


del programlama_dilleri[0] #0. indexteki elemanı sil.

for dil in programlama_dilleri: 
    print(dil)


print(sonuc)