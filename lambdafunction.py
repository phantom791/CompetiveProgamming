import functools

numbers = [x for x in range(1,12) if x!= 10]

squares = list(map(lambda x: x*x, numbers)) 

even = list(filter(lambda x: x%2==0, numbers))


product = functools.reduce(lambda x, y: x*y, numbers)

#funrun = list(functools.accumulate(lambda x, y: x*y, numbers))

print(numbers)

print("sq",squares)

print(product)

print(even)

#print(funrun)
