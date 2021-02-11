# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")
def rotateArray(array):
    '''start = 0                    #swapping 2 elements
    end = len(array)-1
    while(start<end):
        array[start],array[end] = array[end],array[start]
        #print(array)
        start+=1
        end-=1'''
   
    for i in range(len(array)-2,-1,-1):     #one at a time
        array.append(array[i])
        array.pop(i)
   
    return array    
       
ra = rotateArray([1,2,5,45,0,-1,68,9,62,30])
print(ra)