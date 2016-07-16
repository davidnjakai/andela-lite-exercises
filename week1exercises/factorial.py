def factorial(mynum):
	if mynum == 0:
		return 1
	if mynum == 1:
		return 1
	return mynum * factorial(mynum - 1)