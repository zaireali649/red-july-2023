import random

var = []

print(type(var))

print(type("hello"))

var2 = [151, 251, 386, 493, 649, "009"]

print(var2)

var2 = var2 + [721] # not inplace

print(var2)

var2.append(445) # inplace function

print(var2)

print(dir(var2))

var2.reverse()
print(var2)

var3 = [0, 1, 2, 3, 4, 5]

print(var3)

numbers = range(0, 20)
print(numbers)
print(type(numbers))
numbers = list(numbers) # type casting
print(type(numbers))
print(numbers)

for number in numbers:
    print(number * 2)
    
for i in range(0, 10):
    print(i**3)
    
numbers2 = [0, 2, 4, 6, 8]
print(numbers2)

print(numbers2[3])

print(numbers2[-1])

print(len(numbers2))

# print(numbers2[len(numbers2)]) dont do this. It wil get IndexError

lol = [
    [random.randint(0, 10), random.randint(0, 10), random.randint(0, 10)],
    [random.randint(0, 10), random.randint(0, 10), random.randint(0, 10)],
    [random.randint(0, 10), random.randint(0, 10), random.randint(0, 10)],
    [random.randint(0, 10), random.randint(0, 10), random.randint(0, 10)]
    ]
    
print(lol)

for element in lol:
    print(element)
    for ele in element:
        print(ele)