import random

var = []  # Empty list

print(type(var))  # Output: <class 'list'>, printing the type of var

print(type("hello"))  # Output: <class 'str'>, printing the type of the string "hello"

var2 = [151, 251, 386, 493, 649, "009"]  # List containing integers and a string

print(var2)  # Output: [151, 251, 386, 493, 649, '009'], printing the list var2

var2 = var2 + [721]  # Adding a new element (721) to var2 without modifying it in place

print(var2)  # Output: [151, 251, 386, 493, 649, '009', 721], printing the updated list var2

var2.append(445)  # Appending 445 to var2 in place

print(var2)  # Output: [151, 251, 386, 493, 649, '009', 721, 445], printing the updated list var2

print(dir(var2))  # Output: A list of available attributes/methods of var2

var2.reverse()  # Reversing the order of elements in var2 in place
print(var2)  # Output: [445, 721, '009', 649, 493, 386, 251, 151], printing the reversed list var2

var3 = [0, 1, 2, 3, 4, 5]  # List containing integers

print(var3)  # Output: [0, 1, 2, 3, 4, 5], printing the list var3

numbers = range(0, 20)  # Generating a range object from 0 to 19

print(numbers)  # Output: range(0, 20), printing the range object

print(type(numbers))  # Output: <class 'range'>, printing the type of numbers

numbers = list(numbers)  # Converting the range object into a list

print(type(numbers))  # Output: <class 'list'>, printing the type of numbers after conversion
print(numbers)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], printing the list numbers

for number in numbers:
    print(number * 2)  # Output: Each element of the list numbers multiplied by 2

for i in range(0, 10):
    print(i**3)  # Output: Cubes of numbers from 0 to 9

numbers2 = [0, 2, 4, 6, 8]  # List containing even numbers

print(numbers2)  # Output: [0, 2, 4, 6, 8], printing the list numbers2

print(numbers2[3])  # Output: 6, accessing the element at index 3

print(numbers2[-1])  # Output: 8, accessing the last element using negative indexing

print(len(numbers2))  # Output: 5, printing the length of the list numbers2

# print(numbers2[len(numbers2)]) don't do this. It will get IndexError
# The above line tries to access an element outside the list bounds, causing an IndexError.

lol = [
    [random.randint(0, 10), random.randint(0, 10), random.randint(0, 10)],  # A 3-element list with random integers
    [random.randint(0, 10), random.randint(0, 10), random.randint(0, 10)],  # A 3-element list with random integers
    [random.randint(0, 10), random.randint(0, 10), random.randint(0, 10)],  # A 3-element list with random integers
    [random.randint(0, 10), random.randint(0, 10), random.randint(0, 10)]   # A 3-element list with random integers
]

print(lol)  # Output: A list of lists containing random integers

for element in lol:  # Looping through the outer list
    print(element)  # Output: Each inner list containing random integers
    for ele in element:  # Looping through each inner list
        print(ele)  # Output: Each random integer inside the inner lists
