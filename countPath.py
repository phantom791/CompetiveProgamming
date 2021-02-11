def countPath(m,n):
	rows,cols = m,n
	arr = [[0]*cols]*rows
	#arr = [[0 for j in range(cols)] for i in range(rows)]
	print(arr)
	for x in range(rows):
		arr[x][0] = 1
	for y in range(cols):
		arr[0][y] = 1
		
	print(arr)	
		
	for i in range(1,cols):
		for j in range(1,rows):
			arr[i][j] = arr[i-1][j] + arr[i][j-1]
	
	print(arr)	
		
	return arr[m-1][n-1]

noOfPaths = countPath(6,6)
print(noOfPaths)	