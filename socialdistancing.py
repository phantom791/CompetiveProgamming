import math
def socialDistancing(s,k):
	#count = 0
	#Flag = False
	l = list(s)
	edge = l.index('1')
	if edge>=k+1:
		edge = 0
		l[edge] = '1'
	c = l.count('1')
	count = 1
	def iterate(l,k,edge,c,count):
		counter = 0
		s = ''
		if c == count:
			for element in l:
				s+=element
			#print(s)
			return s
		else:
			for x in range(edge+1,len(l)):
				if not l[x] == '1':
					counter += 1
				else:
					edge = x
					n = k+1
					while(counter>k):
						#print(counter,k,x,x-n)
						mid = math.ceil(counter/2)
						#print(mid)
						if mid>k:
							#print(counter,k,x,x-n)
							l[x-n] = '1'
							n += k+1
						counter -= k+1
					count += 1
					#print(l)
					return iterate(l,k,edge,c,count) 
					
	return iterate(l,k,edge,c,count)
	

z = socialDistancing("00000010000010000000001",2)
print(z)


'''c = 0 # global variable

def add():
    global c
    c = c + 2 # increment by 2
    print("Inside add():", c)

add()
print("In main:", c)'''