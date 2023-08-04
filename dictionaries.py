import random

var = {}  # Empty dictionary

print(type(var))  # Output: <class 'dict'>, printing the type of var which is a dictionary

var2 = {"juice": "cranberry", "movie": "The Lion King"}  # Dictionary with key-value pairs

print(var2)  # Output: {'juice': 'cranberry', 'movie': 'The Lion King'}, printing the dictionary var2

print(var2["movie"])  # Output: The Lion King, accessing the value corresponding to the key "movie"

var2["drank"] = "patron"  # Adding a new key-value pair to var2

print(var2)  # Output: {'juice': 'cranberry', 'movie': 'The Lion King', 'drank': 'patron'}, printing the updated dictionary var2

var2["movie"] = "Interstellar"  # Modifying the value corresponding to the key "movie"

print(var2)  # Output: {'juice': 'cranberry', 'movie': 'Interstellar', 'drank': 'patron'}, printing the updated dictionary var2

del var2["drank"]  # Deleting the key-value pair with key "drank" from var2

print(var2)  # Output: {'juice': 'cranberry', 'movie': 'Interstellar'}, printing the updated dictionary var2

var2["movie"] = [var2["movie"], "The Lion King"]  # Modifying the value corresponding to the key "movie" with a list

print(var2)  # Output: {'juice': 'cranberry', 'movie': ['Interstellar', 'The Lion King']}, printing the updated dictionary var2

var2["fruit"] = "mango"  # Adding a new key-value pair to var2

print(var2)  # Output: {'juice': 'cranberry', 'movie': ['Interstellar', 'The Lion King'], 'fruit': 'mango'}, printing the updated dictionary var2

print(dir(var2))  # Output: A list of available attributes/methods of var2

print(list(var2.keys()))  # Output: ['juice', 'movie', 'fruit'], printing the list of keys in var2

print(list(var2.values()))  # Output: ['cranberry', ['Interstellar', 'The Lion King'], 'mango'], printing the list of values in var2

for k, v in var2.items():  # Looping through key-value pairs in var2
    print(k, v)  # Output: Each key and its corresponding value in var2

dol = {
    1: [random.randint(0, 10), random.randint(0, 10), random.randint(0, 10)],  # A list of random integers as value for key 1
    2: [random.randint(0, 10), random.randint(0, 10), random.randint(0, 10)],  # A list of random integers as value for key 2
    3: [random.randint(0, 10), random.randint(0, 10), random.randint(0, 10)],  # A list of random integers as value for key 3
    4: [random.randint(0, 10), random.randint(0, 10), random.randint(0, 10)]   # A list of random integers as value for key 4
}

for key, value in dol.items():  # Looping through key-value pairs in dol
    print(key, value)  # Output: Each key and its corresponding value in dol
    for element in value:  # Looping through each list in the values of dol
        print(element)  # Output: Each element (random integer) in the inner lists of dol
