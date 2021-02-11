def oneone(seq,n,count):
	temp = ''
	temp_count = 1
	#if len(seq)==1:
	#	temp+=str(temp_count)+seq
	if not len(seq)==1:
		if count>n:
			return seq
		else:
			for i in range(len(seq)-1):
				t = seq[i]
				if seq[i+1]==seq[i]:
					temp_count+=1
				else:
					temp+=str(temp_count)+str(t)
					temp_count=1
			if seq[-1]==seq[-2]:
				temp = temp[:-2]+str(int(temp[-2])+1)+temp[-1]
			else:
				temp = temp+str(temp_count)+str[-1]
	
			return oneone(temp,n,count+1)
	else len(seq)==1:
		temp+=str(temp_count)+seq







count = 1
o = oneone('1',1,count)
print(o)
	