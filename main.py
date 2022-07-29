# Barcha kompyuterda mavjud bo\'lgan harflar, smayliklar... sayti: https://unicode-table.com/en/emoji/

# STRING BILN ISHLASH

# title
# ism_fam='abduhalilov mubosher'
# print(ism_fam.title()) # har bir so'zni boshini katta harf qiladi

#strip
# meva = '       banan      '
# print('Men '+meva.lstrip()+'ni yaxshi ko\'raman') # chapdagi bo'shliqni o'chiradi
# print('Men '+meva.rstrip()+'ni yaxshi ko\'raman') # o'ngdagi bo'shliqni o'chiradi
# print('Men '+meva.strip()+'ni yaxshi ko\'raman') # ikkala tomondagi bo'shliqni o'chiradi
# print('Men '+meva+'ni yaxshi ko'raman)

# map va range
# sonlar=list(range(1,20)) # malum bir sondan malum bir songacha bo'lgan ketma ketlik
# print(sonlar)
#
# kvadrat = lambda x: x**2
# kvadrat_ildiz = lambda x: x**.5
# kvadratlar=list(map(kvadrat,sonlar)) # bir funksiyani malum bir listdagi barcha elementlariga qollaydi
# print(kvadratlar)

# a = [1, 2, 3]
# b = [4, 5, 6]
# a_plus_b = list(map(lambda x,y: x+y,a,b))
# print(a_plus_b)

# sample va filter
# import random as r
# sonlar = r.sample(range(1,100),10) # biror list ichidan x ta tasodifiy sonlarni olish
# juftmi = lambda x: x%2 == 0
# juft_sonlar=list(filter(juftmi,sonlar)) # listdan qaytgan javobga(True,False) binoan filtrlaydi
# print(sonlar)
# print(juft_sonlar)

# mevalar = ['anor', 'olma', 'olcha', 'banan', 'anjir', 'apelsin', 'do\'lana']
# harf='o'
# mev_ajr = lambda meva: meva.startswith(harf)
# filtr_mevalar = list(filter(mev_ajr,mevalar))
# print(filtr_mevalar)
