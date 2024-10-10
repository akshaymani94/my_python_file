employees = ["aks","dg","suk","mad"]

file_path = "output2.txt"
# file_path = "/home/mechfoam/Desktop/output.txt"

with open(file_path,"w") as file:
    for employee in employees:
        file.write(employee+"\n")
    print(f"txt file '{file_path}' was created")
