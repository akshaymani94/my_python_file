import csv

file_path = "output.csv"

try:
    with open(file_path,"r") as file:
        content = csv.reader(file)
        for line in content:
            # print(line)
            print(line[2])


except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You dont have permission to read that file")    