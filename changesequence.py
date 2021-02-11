from itertools import combinations
def changeSequence(string,n):
	a = combinations(string,n)
	l = [' '.join(i) for i in a]

	print(l)


changeSequence('12345',3)