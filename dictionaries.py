import random

var = {}

print(type(var))

var2 = {"juice": "cranberry", "movie": "The Lion King"}

print(var2)

print(var2["movie"])

var2["drank"] = "patron"

print(var2)

var2["movie"] = "Interstellar"

print(var2)

del var2["drank"]

print(var2)

var2["movie"] = [var2["movie"], "The Lion King"]

print(var2)

var2["fruit"] = "mango"

print(var2)

print(dir(var2))

print(list(var2.keys()))

print(list(var2.values()))

for k, v in var2.items():
    print(k, v)
    
dol = {
    1: [random.randint(0, 10), random.randint(0, 10), random.randint(0, 10)],
    2: [random.randint(0, 10), random.randint(0, 10), random.randint(0, 10)],
    3: [random.randint(0, 10), random.randint(0, 10), random.randint(0, 10)],
    4: [random.randint(0, 10), random.randint(0, 10), random.randint(0, 10)]
    }
    
for key, value in dol.items():
    print(key, value)
    for element in value:
        print(element)