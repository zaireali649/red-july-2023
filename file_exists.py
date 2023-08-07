import os

# Check if the directory name "red-july-2023" is not in the last part of the current working directory's path.
if "red-july-2023" not in os.getcwd().split('/')[-1]:
    # If not present, change the working directory to "red-july-2023".
    os.chdir("red-july-2023")
    # Print a message to indicate that the working directory has been changed.
    print("Changed working directory")

# Print the current working directory after the potential change.
print(os.getcwd())

# Check if the file "cities.py" exists in the current working directory.
print(os.path.exists("cities.py"))
