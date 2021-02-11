# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")
class SortNegative:
    def __init__(self):
        self.base_index = 0
   
    def sort(self,array):
        for index in range(len(array)):
            if array[index]<0:
                array.insert(self.base_index,array[index])
                array.pop(index+1)
                self.base_index+=1
               
        return array        
       
   
obj = SortNegative()
sorted_array = obj.sort([-1,-20,1,2,1,-10,2,1,-2,0,1,-1,2,0,-12,1,-2,0,1,2,0,1,1,-2,0,1,2,0])
print(sorted_array)