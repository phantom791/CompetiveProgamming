def smallestNumber(n):
	for i in range(10):
		for j in range(10):
			if i != j and i+j == n:
				if i == 0:
					return j
				return i*10 + j
	return -1				
					
				
	
print(smallestNumber(0))