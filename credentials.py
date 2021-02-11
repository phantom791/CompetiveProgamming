import os

name = 1
credentials = {}
with open('credentials.txt', 'r') as f:
    for line in f:
        user, pwd = line.strip().split(':')
        credentials[user] = pwd
e = open('h.txt','w')
while os.path.exists("h.txt"):
		os.remove(str(name)+'s.txt')
#while os.path.exists("h.txt"):
	#f = open(str(name)+'s.txt','w')
		name+=1
