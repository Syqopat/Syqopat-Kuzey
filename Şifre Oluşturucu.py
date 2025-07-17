#Rastgele Şifre Oluşturucu

#-------------------------

#Rastgele karakterlerle kullanıcının belirlediği uzunlukta bir şifre oluşturur

#-------------------------

import random

#Tüm karakterleri depolayan değişken.
karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

#Kullanıcıya hoşgeldin mesajı.
print("Rastgele şifre oluşturucuya hoşgeldiniz.\n\n\n")


#Kullanıcıdan şifrenin uzunluğu hakkında değer atanması.
uzunluk_sayisi = int(input("Şifre kaç haneli olsun : "))

#Oluşturulucak olan şifrenin değişkeninin boş hali.
sifre = ""

#Kullanıcıdan alınan uzunluk kadar rastgele karakterlerin üst üste eklenip "sifre" değişkenine atanması.
for x in range(uzunluk_sayisi):
    sifre += random.choice(karakterler)

#Oluşturulan şifrenin ekrana yazdırılması.
print(f"\n\n\nOluşturulan şifre = {sifre}")

#Syqopat Was Here
