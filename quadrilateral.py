import random as R
import math as M

def choice(ch):
	choice_list = []
	for i in range (1,ch+1):
		choice_list.append(i)
	try:
		e = int(input("Enter your Choice: "))
		print("\n")
		if e in choice_list:
			return e
		if e == 0:
			exit()
		else:
			print("Invalid Choice!\t","PLEASE ENTER A VALID CHOICE!!")
			return choice(len(choice_list))
	except ValueError:
		print("Invalid Choice!\t","PLEASE ENTER A VALID CHOICE!!")
		return choice(len(choice_list))


def printFunction(area,perimeter):
	print("Area of the Quadrilateral is :",area,"sq. units")
	print("Perimeter of the Quadrilateral is :",perimeter,"units")


def quadrilateral():
	quad = input("Enter name of quadrilateral: ")
	print("\n")

	if not len(quad) == 4:
		print("The is not a Quadrilateral as it does not have 4 sides")
		return quadrilateral()

	for point in quad:
		if quad.count(point)>1:
			print("The is not a valid Quadrilateral as one or more vertices are repeated")
			return quadrilateral()

	if not quad.isalpha():
		print("Use of numbers of special characters is not allowed")
		return quadrilateral()


	side_list = []
	diagonal_list = []
	diagonal = None
	exit = "Enter 0 to exit"

	
	for i in range(len(quad)-1):
		side_list.append(quad[i]+quad[i+1])
	side_list.append(quad[-1]+quad[0])
	
	diagonal_list.append(quad[0]+quad[2])
	diagonal_list.append(quad[1]+quad[3])
	
	
	print("Assuming that the four sides of the Quadrilateral are given")

	print("Please enter the length of the sides in units")

	for i in range(len(side_list)):
		x = R.uniform(40.0,90.0)
		print("Length of side "+side_list[i]+": "+str(x),"units")
		side_list[i]+=':'+str(x)
	print("\n")

	m = float(side_list[0][3:])
	n = float(side_list[1][3:])
	o = float(side_list[2][3:])
	p = float(side_list[3][3:])

	print("Select one of the following options:")
	print("Enter 1 if one diagonal of the Quadrilateral is given")
	print("Enter 2 if one angle of the Quadrilateral is given")
	print(exit)
	print("\n")

	c = choice(2)

	if c == 1:
		print("Enter 1 if diagonal is",diagonal_list[0])
		print("Enter 2 if diagonal is",diagonal_list[1])
		print(exit)
		print("\n")

		k = choice(2)

		Y = R.uniform(50.0,80.0)

		print("Please enter length of diagonal in units: ",Y)
		print("\n")

		if k == 1:
			diagonal_list[0]+=':'+str(Y)
			diagonal = 1

		if k == 2:
			diagonal_list[1]+=':'+str(Y)
			diagonal = 2


	if c == 2:
		print("Enter 1 if angle is",quad[0])
		print("Enter 2 if angle is",quad[1])
		print("Enter 3 if angle is",quad[2])
		print("Enter 4 if angle is",quad[3])
		print(exit)
		print("\n")

		l = choice(4)

		L = R.randrange(40,170)

		print("Enter angle in degrees: ",L)

		f = M.cos(M.radians(L))
 
		if l == 1:
			x = M.sqrt((m**2)+(p**2)-2*(m*p)*(f))

		if l == 2:
			x = M.sqrt((m**2)+(n**2)-2*(m*n)*(f))

		if l == 3:
			x = M.sqrt((o**2)+(n**2)-2*(o*n)*(f))

		if l == 4:
			x = M.sqrt((o**2)+(p**2)-2*(o*p)*(f))


		if l in [1,3]:
			diagonal_list[1]+=':'+str(x)
			diagonal = 1


		if l in [2,4]:
			diagonal_list[0]+=':'+str(x)
			diagonal = 2


	if diagonal == 1:
		d = float(diagonal_list[0][3:].strip())
		g=((m+n+d)/2)
		h=((o+p+d)/2)
		area=(g*(g-m)*(g-n)*(g-d))+(h*(h-n)*(h-m)*(h-d))

	if diagonal == 2:
		d = float(diagonal_list[1][3:].strip())
		g=((m+p+d)/2)
		h=((n+o+d)/2)
		area=(g*(g-n)*(g-o)*(g-d))+(h*(h-n)*(h-o)*(h-d))

	perimeter = m+n+o+p


	printFunction(area,perimeter)


quadrilateral()
