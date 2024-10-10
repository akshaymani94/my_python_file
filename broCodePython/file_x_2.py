txt_data = "I like business"

file_path = "output.txt"
# file_path = "/home/mechfoam/Desktop/output.txt"

try:
    with open(file_path,"x") as file:
        file.write(txt_data)
        print(f"txt file '{file_path}' was created")
except FileExistsError:
    print("That file already exists")

# w is for write
# r is for read
# x will write if file doesnt exits
