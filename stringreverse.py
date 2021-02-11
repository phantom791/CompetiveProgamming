import random

def stringReverse(string):
	global reversed_string 						#change in this variable will affect the variable reversed_string outside the function to change
	if len(string) == 0:
		return 
	else:
		reversed_string+=string[-1]
		stringReverse(string[:-1])

def check_palindrome(string,reversed_string):
	if not string == reversed_string:
		print("String is not a palindrome")
		return False
	return True

reversed_string = "" 
string_list = ["ndsnkjh","salflash","asdgdsa","malayalam","kjkjfafmf"]
string = random.choice(string_list)


stringReverse(string)
print("Original String is:",string)					#to show string is immutable (int, float, bool, str, tuple, unicode) // mutable (list, set, dict)
print("Reversed String is:",reversed_string)

if check_palindrome(string,reversed_string):
	print("String is a palindrome")