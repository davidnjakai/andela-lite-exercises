def sum_of_unique_digits(A):
	strlist = []
	ans = 0
	for num in A:
		strlist.append(str(num))

	digits = ''.join(strlist)

	for digit in set(digits):
		ans += int(digit)

	return ans