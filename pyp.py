import os
import random
import math
import tkinter
def fib(limit):
	a = [0,1]
	for i in range(1,limit+1):
		a.append(a[i]+a[i-1])
	print (a)
	z = input("enter")
	print(z)

def filedemo():
	if os.path.exists("r.txt"):
		os.remove("r.txt")
	else:
		print("file does not exist")
	#os.rmdir("myfolder")
	f = open("a.txt")
	#f.write("more content")
	#f.close()
	#print(f.read())
	#print(f.readline())
	#print(f.readline())
	#for x in f:
		#print(x)
	e = open("x.txt","w")
	#print(e.read())
	for x in f:
		e.write(x)
	#print(f.read())
	e.close()
	f.close()
	z = open("x.txt")
	print(z.read())
	#os.remove

	#with open("x.txt") as a:
		#with open("a.txt","w") as b:
			#for x in a:
				#b.write(x)
	#b.close()
	#a = open("a.txt")
	#print(a.read())




def cowsnbulls(num):
	l = []
	b = ""
	a = str(random.randrange(1000,math.pow(10,num)))
	while len(b) !=num:
		b = input("guess the number: "+str(num)+" digits: ")
	#print(a)
	#print(type(b))
	for x in range(0,len(a)):
		#print(a[x])
		if a[x] == b[x]:
			#if a.index() == b.index():
			l.append("cow")
		else:
			l.append("bull")
	print("Generated No: "+":"+a)
	print("Your Guess: "+":"+b)
	print("cows"+":"+str(l.count("cow"))+"  "+"bulls"+":"+str(l.count("bull")))
	if l.count("cow")>l.count("bull"):
		print("Congratulations You won!!")
	else:
		print("Better Luck Next Time")


	

#def get_player_name():
    #print()
    #player_name = ""
    #while len(player_name) !=4: 
        #player_name = input('Please enter your name: ')
        #print()
    #return player_name

def div():
	l=[]
	for i in range(2000, 3201):
		if (i%7==0) and (i%5!=0):
			l.append(str(i))
	print (','.join(l))


class Parrot:
	species  = "bird"  #class attribute

	def __init__(self,name,age):
		self.name = name  #instance attribute
		self.age = age

	def sing(self,song):
		return "{} sings {}".format(self.name,song)

	def dance(self):
		return "{} is now dancing".format(self.name)


#blu = Parrot("blu",10)
#woo = Parrot("woo",15)

#print("Blu is a {}".format(blu.__class__.species))
#print("Woo is also a {}".format(woo.__class__.species))

#print("{} is {} years old".format(blu.name,blu.age))
#print("{} is {} years old".format(woo.name,woo.age))

#print(blu.sing("Happy"))
#print(blu.dance())

class Bird:       #inheritance
	def __init__(self):
		print("Bird is ready")

	def whoIsThis(self):
		print("Bird")

	def swim(self):
		print("Swim faster")

class Penguin(Bird):
	def __init__(self):
		super().__init__()
		print("Penguin is ready")

	def whoIsThis(self):
		print("Parrot")

	def run(self):
		print("Run faster")


#peggy = Penguin()
#peggy.whoIsThis()
#peggy.swim()
#peggy.run()


class Computer:   #encapsulation

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):    #setter function
        self.__maxprice = price

#c = Computer()
#c.sell()
#
## change the price
#c.__maxprice = 1000
#c.sell()
#
## using setter function
#c.setMaxPrice(1000)
#c.sell()


class Parrot:           #polymorphism

	def fly(self):
		print("Parrot can fly")

	def swim(self):
		print("Parrot cant swim")


class Penguin:
	
	def fly(self):
		print("Penguin cant fly")

	def swim(self):
		print("Penguin can swim")

def flying_test(bird):
	bird.fly()

def swimming_test(bird):
	bird.swim()

#peggy = Penguin()
#blu = Parrot()

#flying_test(blu)
#flying_test(peggy)

#swimming_test(blu)
#swimming_test(peggy)

from tkinter import *
from tkinter import filedialog
#from tkFileDialog   import askopenfilename

def NewFile():
    print ("New File!")
def OpenFile():
    name = filedialog.askopenfilename()
    print (name)			
def About():
    print ("This is a simple example of a menu")
    
root = Tk()
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open...", command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)

#mainloop()


def check_anagram(first,second):
	a = "Not an anagram"
	b = "Anagram detected"
	if len(first) == len(second):
		for i in range(0,len(first)):
			for j in range(0,len(second)):
				if first[i] in second:
					if second[j] in first:
						if first[i] != second[i]:
							print("Anagram")
						return a
					return a
				return a
			#return False
	return a

check_anagram("left","flt")






