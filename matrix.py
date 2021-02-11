import random

def matrix():
	binary_list = [0,1," ","","","",""]
	while True:
		binary = random.choice(binary_list)
		print(binary,end="")

matrix()

