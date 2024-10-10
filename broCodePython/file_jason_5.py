import json
employees = {
    "name" : "Akshay",
    "age"   : 29,
    "job"   : "CFD Engineer"
}

file_path = "output.json"
# file_path = "/home/mechfoam/Desktop/output.json"

with open(file_path,"w") as file:
    json.dump(employees,file,indent = 4)
    print(f"json file '{file_path}' was created")
