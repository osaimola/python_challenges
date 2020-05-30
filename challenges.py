"""
Create a function that takes a 2D array as an argument and returns
the number of people whose view is blocked by a tall person. The concert
stage is pointed towards the top of the 2D array and the tall person
(represented by a 2) blocks the view of all the people (represented by a 1)
behind them.
https://edabit.com/challenge/E9FwvGyad5CDbiH4C
"""
def block(lst):
	rows = len(lst) - 1
	blocked = 0
	for i in range(rows):
		blocked += (lst[i].count(2) * (rows - i))
	return blocked


"""
The additive persistence of an integer, n, is the number of times you have to replace n with the sum of its digits until n becomes a single digit integer.
The multiplicative persistence of an integer, n, is the number of times you have to replace n with the product of its digits until n becomes a single digit integer.

Create two functions that take an integer as an argument and:
1. return its additive persistence
2. return its multiplicative persistence
https://edabit.com/challenge/5ou6SKDtFRZugbpda
"""
def additive_persistence(n):
	if n < 10:
		return 0
	
	def sum_n(x):
		result = 0
		while x:
			result, x = result + x % 10, x // 10
		return result

	return 1 + additive_persistence(sum_n(n))
	

def multiplicative_persistence(n):
	if n < 10:
		return 0
	
	def product_n(x):
		result = 1
		while x:
			result, x = result * (x % 10), x // 10
		return result

	return 1 + multiplicative_persistence(product_n(n))


"""
In this challenge, transform a string into a series of words (or sequences of characters) separated by a single space, with each word having the same length given by the first 15 digits of the decimal representation of Pi:
3.14159265358979
https://edabit.com/challenge/sHJmjMcZPiCsEujk6
"""
def pilish_string(txt):
	pi = "314159265358979"
	output = []
	a, b = 0, 0
	char_count = 0
	try:
		for pi_char in pi:
			a = b
			b = a+int(pi_char)
			if txt[a:b] != "":
				output.append(txt[a:b])
				char_count = int(pi_char)
				continue
			break
	finally:
		try:
			#check that last item in list is long enough, if not extend.
			if len(output[-1]) < int(char_count):
				output[-1] = output[-1] + (output[-1][-1]* (char_count-len(output[-1])))
		except(IndexError):
			pass
	return " ".join(output)