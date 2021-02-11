def factorial(n):					#recursion
	if n<0:
		return -1
	if n == 0 or n== 1:
		return 1
	else:
		return n*factorial(n-1)
	
memo =[]

def memoFact(N):						#memoisation
    arr={}
    if N in arr:
        return arr[N]
    elif N == 0 or N == 1:
        return 1
        arr[N] = 1
    else:
        factorial = N*memoFact(N - 1)
        arr[N] = factorial
    return factorial

def dpFact(n):
	if n<0:
		return -1
	if n == 0 or n == 1:
		return 1
	memo[0] = 1
	for i in range(1,n+1):
		memo[i] = memo[i-1]*i
	return memo[n]


a = int(input("enter: "))
print(factorial(a))
