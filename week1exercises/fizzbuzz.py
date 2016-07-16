def fizz_buzz(mynum):
	if mynum % 15 == 0:
		return 'FizzBuzz'
	if mynum % 5 == 0:
		return 'Buzz'
	if mynum % 3 == 0:
		return 'Fizz'
	return mynum