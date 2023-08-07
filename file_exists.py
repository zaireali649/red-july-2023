import os

if "red-july-2023" not in os.getcwd().split('/')[-1]:
    os.chdir("red-july-2023")
    print("Changed working directory")


print(os.getcwd())
print(os.path.exists("cities.py"))