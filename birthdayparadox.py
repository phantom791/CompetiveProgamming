import math
def birthdayparadox(p):
	return math.ceil(math.sqrt(2*365*math.log(1/(1-p))))

print(birthdayparadox(0.999))