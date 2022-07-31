def word_to_harf(word, ch):
	fil_gue_word=[]
	w = ch
	s = 0
	for i in word:
		s += 1
		if s > 1:
			len_low_thr = word[s-2:s]
			if len_low_thr in ['ch',"o'",'sh']:
				fil_gue_word.append(len_low_thr)
				s += 1
			elif len_low_thr != '':
				if s == len(w)-1:
					fil_gue_word.append(len_low_thr[0])
					fil_gue_word.append(len_low_thr[1])
					s += 1
				else:
					fil_gue_word.append(len_low_thr[0])
	return fil_gue_word
def unl_text(fl_gue_w,ls,harf):
	count=0
	for i in fl_gue_w:
		if i == harf:
			ls[count] = i
		count += 1
	return ''.join(ls)
def my_isalpha(word):
	ajr_word = ""
	for i in word:
		if i != "'":
			ajr_word += i
	return ajr_word.isalpha()