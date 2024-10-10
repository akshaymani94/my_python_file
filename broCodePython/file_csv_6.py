
import csv

employees = [["Name","Age","Job"],
            ["aks",30,"CFD"],
            ["deep",29,"CSE"],
            ["prav",28,"BSC"]]

file_path = "output.csv"

try:
    with open(file_path,"w") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"csv file {file_path} was created")
except FileExistsError:
    print("That file already exists")