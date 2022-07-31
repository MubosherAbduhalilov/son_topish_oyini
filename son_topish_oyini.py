while True:
	from random import randint
	print('Keling o\'ylagan sonni topish o\'yinini o\'ynaymiz!!!')
	kom_son = randint(1,11)
	guess = int(input('Men bir son o\'yladim. Topa olasizmi?:\n>>> '))
	for i in range(1,11):
		if guess == kom_son:
			guess_quan_of_user = i
			print(f'Tabriklayman siz javobni {i} ta urinishda topdingiz')
			break
		elif guess < kom_son:
			guess=int(input('Xato, men o\'ylagan son bundan kattaroq. Yana harakat qiling:\n>>> '))
		else:
			guess=int(input('Xato, men o\'ylagan son bundan kichikroq. Yana harakat qiling:\n>>> '))
	print('1 dan 10 gacha son o\'ylang. Men topishga harakat qilaman')
	input('Agar o\'ylagan bo\'lsangiz istalgan tugmani bosing ')
	sr=1
	sp=10
	for i in range(1,10):
		com_gue=randint(sr,sp)
		javob = input(f"Siz {com_gue} ni o\'yladingiz: to\'g\'ri(t),"
					  f"men o\'ylagan son bundan kattaroq(+), yoki kichikroq(-) ")
		if javob == 't':
			if i == guess_quan_of_user:
				print(f'Ikkalamiz ham {i} urinishda topdik\nDurrang!!!')
			elif i < guess_quan_of_user:
				print(f'Men {i} urinishda topdim\nSiz {guess_quan_of_user} urinishda topdingiz\nMen g\'olibman!!!')
			else:
				print(f'Men {i} urinishda topdim\nSiz {guess_quan_of_user} urinishda topdingiz\nSiz g\'olibsiz!!!')
			break
		if javob == '-':
			sp = com_gue - 1
		if javob == '+':
			sr = com_gue + 1
	res=input('Yana o\'ynashni xoxlaysizmi: ha(1) / yo\'q(0): ')
	if res == '1':
		continue
	else:
		break