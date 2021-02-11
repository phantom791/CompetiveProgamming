# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")
def unionIntersection(array1,array2):
    union_set = []
    intersection_set = []
   
    for element1 in array1:
        union_set.append(element1)
    for element2 in array2:
        #if element2 not in array1:
        if element2 in union_set:
            intersection_set.append(element2)
        else:        
            union_set.append(element2)
           
           
   
    return union_set,intersection_set
   
   
union_set,intersection_set = unionIntersection([16,1,2,5,4,10,7],[1,2,5,7,8,12,6]) #returnig two values

print(union_set)
print(intersection_set)