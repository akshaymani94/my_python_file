txt_data = "I like business"

file_path = "output.txt"
# file_path = "/home/mechfoam/Desktop/output.txt"

with open(file_path,"w") as file:
    file.write(txt_data)
    print(f"txt file '{file_path}' was created")

# w is for write
# r is for read
# x will write if file exits
