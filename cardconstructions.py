import random
def cardConstructions(n):
	level_counter = [0]
	level = 0
	cards_required = 0
	if (n>1):
		print("Maxed pyramids possible:")
		while (n>=cards_required):
			cards_required = 2+level*3+level_counter[level]
			if(n>=cards_required):			
				level_counter.append(cards_required)
				level+=1

		n = n-level_counter[level]
		print("A pyramid of level",level,"containing", level_counter[level],"cards")

		while(n>0):
			for cards in reversed(level_counter):
				if(n>=cards) and cards!=0:
					print("A pyramid of level",level_counter.index(cards),"containing", cards,"cards")
					n = n-cards

			if n==1:
				print('\n')
				print("Card left:", n) 
				break

n = random.randint(1,1000) 
print("Total number of cards: ",n)
cardConstructions(n)