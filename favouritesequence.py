def favouriteSequence(sequence):
	restored_sequence = []
	#l = len(sequence)
	while(len(sequence)!=0):
		for i in range(len(sequence)):
			restored_sequence.append(sequence[i])
			sequence = sequence[1:]
			#print(len(sequence),sequence,restored_sequence)
			break
		for j in reversed(range(len(sequence))):
			restored_sequence.append(sequence[j])
			sequence = sequence[:-1]
			#print(len(sequence),sequence,restored_sequence)
			break
	#print(restored_sequence)
	return restored_sequence	
	
print(favouriteSequence([8,4,3,1,2,7,8,7,9,4,2]))