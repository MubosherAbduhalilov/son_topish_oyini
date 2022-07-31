from uzwords import uzwords_ls
from functions import word_to_harf, unl_text, my_isalpha
import random
print('Keling so\'z topish o\'yini o\'ynaymiz.\n'
	  'Bu o\'yinni o\'ynash uchun ikki ishtirokchi bo\'lishi kerak.\n'
	  'Men 5 ta harfdan iborat so\'z o\'ylayman\n'
	  'Siz uni topishga harakat qilib ko\'rasiz')
print("Eslatma: sh, ch, o' kabi harflar bitta harf deb qabul qilinadi")

enemy1 = input('Birinchi o\'yinchi ismi >>> ')
enemy2 = input('Ikkinchi o\'yinchi ismi >>> ')
guesses = []

for i in range(2):
	guess_word = random.choice(uzwords_ls)
	fil_guess_word = word_to_harf(guess_word, ch=guess_word)
	top_har = '-----'
	ls = []
	guess = 0
	print(f'{i+1}-chi o\'yinchi uchun:')
	while not my_isalpha(top_har):
		print(top_har.upper())
		kir_harf = input('Yuqoridagi so\'zni topish uchun harf kiriting >>> ')
		if kir_harf in ls:
			print('Kechirasiz bu harfni oldin kiritgansiz!!!')
		elif kir_harf not in fil_guess_word:
			print('Bunday harf mavjud emas. Davom eting')
			guess += 1
		if kir_harf not in ls:
			ls.append(kir_harf)
			top_har_ls = word_to_harf(top_har, ch=fil_guess_word)
			top_har = unl_text(fil_guess_word, top_har_ls, kir_harf)
			guess += 1
	guesses.append(guess)
	print(top_har.upper())
	print(f'Siz bu so\'zni {guess} urinishda topdingiz')
	if i==0:
		input('Davom etish uchun Enter tugmasini bosing!')
if guesses[0]<guesses[1]:
		print(f"{enemy1} {guesses[0]} urinishda topdi.{enemy2} {guesses[1]} urinishda topdi.{enemy1} g'olib")
else:
		print(f"{enemy1} {guesses[0]} urinishda topdi.{enemy2} {guesses[1]} urinishda topdi.{enemy2} g'olib")
