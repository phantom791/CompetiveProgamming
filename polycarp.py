def polycarp(n):
	x = n//2020 + 1
	#print(x)
	for i in range(x):
		for j in range(x):
			if 2020*i + 2021*j == n:	
				return 'YES'
	return 'NO'			
	

print(polycarp(4043))	