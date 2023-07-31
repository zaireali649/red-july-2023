import random

number = random.randint(0,10)

thresh = 5

if number > thresh:
    print("Big Number")
    
    
if number > thresh:
    print("Big Number")
elif number < thresh:
    print("Small Number")
else: # elif number == thresh:
    print("Number is", thresh)
    
print(number)