def lcsw(stringlist):
	list1  = []
	list2  = []
	listlist  = [list1,list2]
	count = 0
	comparisonlist = []
	for string in stringlist:
		temp_string = string
		temp_list = listlist[count]
		for i in range(len(temp_string)):
			str_new = temp_string[i]
			for j in range(i+1, len(temp_string)):
				str_new += temp_string[j]
				listlist[count].append(str_new)
		count += 1

	for element in list1:
		if element in list2:
			comparisonlist.append(element)

	print(comparisonlist)
	if len(comparisonlist)>0:
		max_len = 0
		temp_list_new = []
		for element in comparisonlist:
			length = len(element)
			if length>max_len:
				max_len = length

		for element in comparisonlist:
			if len(element) == max_len:
				temp_list_new.append((element))

		if len(temp_list_new)>1:
			print("longest common subwords are",temp_list_new,"of length",max_len)
		#lcsw = max(comparisonlist,key=len)
		else:
			lcsw = max(comparisonlist,key=len)
			print("longest common subword is",lcsw,"of length",len(lcsw))
	else:
		print("There is no common subword")


lcsw(['gcdehgof','abcdegofk'])



