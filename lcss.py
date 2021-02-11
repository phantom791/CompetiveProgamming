def LCSNaive(X,Y,m,n):
	if m == 0 or n == 0:
		return 0
	elif X[m-1] == Y[n-1]:
		return 1 + LCSNaive(X,Y,m-1,n-1)
	else:
		return max(LCSNaive(X, Y, m, n-1), LCSNaive(X,Y,m-1,n))

X = 'AGGTAB'
Y = 'GXTXAYB'

#print('length of LCS is', LCSNaive(X, Y, len(X), len(Y)))


def LCSDP(X,Y):
	# find the length of the strings 
    m = len(X) 
    n = len(Y) 
  
    # declaring the array for storing the dp values 
    L = [[None]*(n + 1) for i in range(m + 1)] 
  
    """Following steps build L[m + 1][n + 1] in bottom up fashion 
    Note: L[i][j] contains length of LCS of X[0..i-1] 
    and Y[0..j-1]"""
    for i in range(m + 1): 
        for j in range(n + 1): 
            if i == 0 or j == 0 : 
                L[i][j] = 0
            elif X[i-1] == Y[j-1]: 
                L[i][j] = L[i-1][j-1]+1
            else: 
                L[i][j] = max(L[i-1][j], L[i][j-1]) 
  
    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1] 
    return L[m][n] 
# end of function lcs 
  
  
# Driver program to test the above function 
X = "AGGTAB"
Y = "GXTXAYB"

print('length of LCS is',LCSDP(X,Y))

