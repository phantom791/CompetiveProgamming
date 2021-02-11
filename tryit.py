import math as m 
'''print("Hello World!")
x = ('apple','banana','cactus')
y = (1,2,3,4)
a = ['no','yes']
b = [True,False]


if len(x) == len(y):
	for i in range(len(x)):
		print(x[i]+'='+str(y[i]))

print(a)
a.append('zero')
print(a)
a.insert(2,'hi')
print(a)
for element in a:
	print(element)


#b = {'e','f','g'}
#print(a)
#print(b)
#print(b[0])'''


'''result=eval(input('Enter an expression'))
print(result)'''

'''import math
x=math.sqrt(15)
print(math.floor(x))'''


'''import math
print (int(math.pow(5,5)))'''

'''name={'naruto':'sasuke','hinata':'kakashi'}
print(name.keys())
print(name.values())'''


'''clan=['uzumaki','uchiha','hyuga','hatake']
named=dict(zip(name,clan))
print(named)
for key , value in named.items():
	print(key,value)'''

'''a=6
b=float(a)
print(type(b))
c=int(b)
print(c)
d=7
print(d<a)
print(int(True0'''

'''import math
print(math.pow(2,5) + math.pow(2,7)+math.pow(2,8)+math.pow(2,10)+math.pow(2,12)+math.pow(2,14)+math.pow(2,17)+math.pow(2,19)+math.pow(2,20)+math.pow(2,21)+math.pow(2,22)+math.pow(2,23))'''

#Area of triangle

'''a=float(input("Enter First side  "))
b=float(input("Enter Seccond side  "))
c=float(input("Enter Third side  "))

s=(a+b+c)/2


print("Semi Perimeter =",s)


area=(s*(s-a)*(s-b)*(s-c))


print("Area of the triangle =",area)'''

#Area of rectangle

'''a=int(input("Enter Length = ")) 
b=int(input("Enter Breadth = "))

area=(a+b)*2

print("Area of Rectangle=",area)'''


#Volume of cylinder
'''r=int(input('Enter Radius of cylinder = '))
h=int(input('Enter Height of cylinder = '))

vol=(3.14*(r**2)*h)

print("Volume of Cylinder = ",vol)'''




#area of Quadrilateral
'''b=float(input("first side of 1st triangle = "))
c=float(input("seccond side of 1st triangle = "))
L=float(input("Enter angle = "))

f = m.cos(m.radians(L))



x = m.sqrt((b**2)+(c**2)-2*(b*c)*(f))


print("third side of triangle",x)

e=float(input("fist side of 2nd triangle ="))
f=float(input("seccond side of 2nd triangle ="))

g=((x+b+c)/2)
h=((x+e+f)/2)


area=(g*(g-x)*(g-c)*(g-b))+(h*(h-x)*(h-e)*(h-f))
#M=fl=oat(input("Enter angle = "))


#area=(((a*b)/2)*math.sin(math.radians(L))) + (((e*f)/2)*math.sin(math.radians(M))) 

print("Area of Quadrilateral = ",area)'''


#program for checking prime number9
flag = True
num=int(input("Enter any mumber :"))
if num>1:
	for i in range(2,num):
		if (num%i)==0:
			print("Its not a prime number")
			flag = False
			break
	if flag:
		print("Its a prime number")


