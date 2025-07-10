meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "NGL": "Tamamen dürüst olmak",
            "AFK":"Ekran başında değilim",
            "BTW":"Bu arada",
            "NT":"İyi denemeydi",
            "GG":"İyi maçtı",
            "NPC":"Gerçek olmayan karakter",
            }

for i in range(5):    
    word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
    
    
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("Bu kelime henüz sözlüğümüze eklenmedi")
