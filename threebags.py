def threeBags(list1, list2, list3):
	'''for arg in s:
		print(arg)
	for key, value in kwargs.items():
		print(key, '=', value)
	this_list = list2	
	#print(list1[1:])	
	while not len(this_list)==0:
		list1[0] -= list2[0]
		this_list = this_list[1:]
		if len(this_list) == 1:
			this_list = list3 
	print(list1)'''
	while not len(list2)==1:
		list1[0] -= list2[0]
		list2 = list2[1:]
		
	while not len(list3)==1:
		list1[0] -= list3[0]
		list3 = list3[1:]
		
	while not len(list1)==1:
		list2[0] -= list1[0]
		list1 = list1[1:]
		
	while not len(list2) == 0:
		list1[0] -= list2[0]
		list2 = list2[1:]
		
	while not len(list3) == 0:
		list1[0] -= list3[0]
		list3 = list3[1:]
		
		
	print(list1,list2,list3)	
			
		
		

#threeBags(list1 = [1,3,4,5], list2 = [4,6,7,2], list3 = [5,9,4,1])
threeBags([1,3,4,5], [4,6,7,2], [5,9,4,1])


#args -- non keyword arguments (passed as tuple)
#kwargs -- keyword arguments{arguments with name e.g x = 4] (passsed as dictionary)