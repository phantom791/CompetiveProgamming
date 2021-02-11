def sharkTooth(tooth_data,*args):
	tooth_count = 0
	row_data = []
	for arg in args:
		row_data.append(arg)
	for j in range(1,tooth_data[0]+1):
		temp_list = []
		for row in row_data:
			if row[0]==j:
				temp_list.append(row[1])
		#print(temp_list)
		if not len(temp_list)==0:	
			tooth_count+=min(temp_list)
			#print(tooth_count)
	if tooth_count<=tooth_data[2]:
		return tooth_count
	return tooth_data[2]
		
count = sharkTooth([2,2,13],[1,13],[2,12])
print(count)