def get_summ(one, two, delimeter='&'):
	if type(one) != str:
		return "Аргумент one не является строкой!"
	elif type(two) != str:
		return "Аргумент two не является строкой!"
	else:
		return "{} {} {}".format(one, delimeter, two).upper()

print(get_summ("Learn", "Python"))