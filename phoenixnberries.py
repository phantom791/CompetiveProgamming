import random

def phoenixnberries(x,y):
	print("no. of shrub: ", m)
	print("max. capacity of basket: ", n)
	blue_buffer = 0
	red_buffer = 0
	count = 0
	shrub_counter = []
	for i in range(1,x+1):
		a = random.randint(1,9)
		b = random.randint(1,9)
		print("enter no. of blue berries in shrub"+str(i)+": ", a)
		print("enter no. of red berries in shrub"+str(i)+": ", b)
		temp_list = [a,b]
		shrub_counter.append(temp_list)
	print(shrub_counter)
	for fruit in shrub_counter:
		if fruit[0]>y or fruit[1]>y:
			a = fruit[0]//y
			b = fruit[1]//y
			c = a+b
			count+=c
			blue_buffer+=fruit[0]-y*a
			red_buffer+=fruit[1]-y*b
		else:
			s = (fruit[0]+fruit[1])
			a = s//y
			count+=a
			if fruit[0]>fruit[1]:
				blue_buffer+=s-y*a
			else:
				red_buffer+=s-y*a
		#print(blue_buffer,red_buffer,count)

	print(blue_buffer,red_buffer)


	p = blue_buffer//y
	q = red_buffer//y
	r = p+q
	if r>=1:
		count+=(r)

	print("The no. of baskets that Phoenix can fill completly: ", count)


m = random.randint(1,6)
n = random.randint(1,6)

phoenixnberries(m,n)

