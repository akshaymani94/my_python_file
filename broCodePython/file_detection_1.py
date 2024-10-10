import os

# file_path = "stuff"
# file_path = "stuff/test.txt"

if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")

    if os.path.isfile(file_path):
        print("This is a file")
    elif os.path.isdir(file_path):
        print("This is a directory")
else:
    print("That location doesn't exist")