# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

def pattern(number):
    n = 1
    i = j = number
    mid = number//2 + 1
    space = 0
    flag = True
    
    for x in range(i):
        if n == mid:
            flag = False
        if j==1:
            for a in range(2):
                for y in range(space):
                    print(" ",end = "")
                print(n)
        else:
            for y in range(space):
                print(" ",end = "")
            for z in range(j):
                print(n,end = "")
            print("")
                
        if flag:
            n+=1
            space+=1
            j-=2
        else:
            n-=1
            space-=1
            j+=2
            
pattern(7)          #assuming that the argument is always an odd number