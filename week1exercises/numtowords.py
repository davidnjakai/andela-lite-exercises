#num_to_word(438483478) should output four three eight four eight three four seven eight

def num_to_word(num):
	numdict = {
	0:'zero',
	1:'one',
	2:'two',
	3:'three',
	4:'four',
	5:'five',
	6:'six',
	7:'seven',
	8:'eight',
	9:'nine',
	}

	diglist = []
	for digit in str(num):
		diglist.append(numdict.get(int(digit)))

	print(' '.join(diglist))
