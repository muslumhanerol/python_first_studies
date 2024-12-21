# string concat //string birleştirme
ad="Müslüm H."
soyAd="Erol"
yas=30
#mesaj="My name is " + ad + " " + soyAd + "." + "I am " + str(yas) + " years old."

#--------

# string format
#mesaj="My name {} {}. I am {} years old.".format(ad, soyAd, yas) # {} içine sırasıyla format içindekiler yerleşir. + operatörünü kullanmadan aynı sonucu aldık. Çıktı= My name Müslüm H. Erol. I am 30 years old.

#mesaj="My name {1} {0}. I am {2} years old.".format(ad, soyAd, yas) # index numaralarını atadık. Çıktı= My name Erol Müslüm H.. I am 30 years old.


#mesaj="My name {a} {s}. I am {y} years old.".format(a=ad, s=soyAd, y=yas) # Takma isim kullanma. Çıktı= My name Müslüm H. Erol. I am 30 years old.

#--------


# f-string

mesaj="My name {a} {s}. I am {y} years old."


print(mesaj)
 