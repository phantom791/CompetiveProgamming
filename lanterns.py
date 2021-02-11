import random

def lanterns(s):
	output_string = ''
	#print(random.choice(['L','R']))
	for i in range(len(s)-1):
		if s[i] == '0':
			output_string += random.choice(['L','R'])
		if int(s[i])<=int(s[i+1]):
			output_string+='R'
	output_string+='L'		
	
	print(output_string)
	

lantern_data = '00311112'	
	
lanterns(lantern_data)	