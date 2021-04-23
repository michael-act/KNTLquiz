def mask_word(word):
	keyword = 'KENTEL'.replace('E', 'O')
	mask_word = list(word[:])
	for i in range(6):
		if word[i] != keyword[i]:
			mask_word[i] = '*'
	return ''.join(mask_word)

check_game = lambda real_word, answer: True if real_word == answer else False