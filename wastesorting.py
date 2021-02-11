def wasteDisposal(wcl,wql):
	flag = True
	for i in range(3):
		if wcl[i]>=wql[i]:
			wcl[i] = wcl[i]- wql[i]
			wql[i] = 0
			#print(wcl[i],wql[i])
		else:
			#print("NO")
			return 'NO'
	
	for i in range(2): 	
		if wcl[i]>=wql[i+3]:
			wcl[i] = wcl[i] - wql[i+3]
			wql[i+3] = 0
		else:
			wql[i+3] = wql[i+3] - wcl[i]
			wcl[i] = 0
		#print(wcl[i],wql[i+3])
			
	if wcl[2]>=wql[3]+wql[4]:
		wcl[2] = wcl[2] - wql[3]-wql[4]
		#print("yes")
		return 'YES'
	return 'NO'	
		
	
waste_capacity_list = [30,37,42]
waste_quantity_list = [0,0,0,40,47]
	
print(wasteDisposal(waste_capacity_list, waste_quantity_list))	