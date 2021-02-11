import random
def solve(x,y):
	solution = [ [ 0 for j in range(y) ] for i in range(x) ] 
	marked = []
	#last = solution[-1]
	#print("g",last)

	def runRat(position):
		next_ = []
		for i in range(last[0]-1,last[0]+2):
			for j in range(last[1]-1,last[1]+2):
				if i>=0 and j>=0 and [i,j] not in marked:
					next_.append([i,j])
					#marked.append([i,j])

		for element in next_:
			if element not in marked:
				solution[position]= element 
				marked.append(element)
				if element==end or reachedAt(element):
					return solution
		return None

	return runRat(1)
	#last = solution = [[0,0]]
	#for i in range()
	#print(solution)
	#print(marked)

def reachedAt(element):
	i = element[0]
	j = element[1]
	if maze[i][j]=='.':
		return True
	return False

x = random.randint(4,10)
y = random.randint(4,10)
p = 0
start = [0,0]
end = [x-1,y-1]
choice = ['.','X','.']

maze = [[random.choice(choice) for j in range(y)] for i in range(x)]
maze[0][0] = maze[0][0] = '.'
while(p<x):
	for q in range(0,y):
		print(maze[p][q],end = "   ")
	print('\n')
	p+=1

#print(maze)

print(solve(x,y))


