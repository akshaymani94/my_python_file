import json

file_path = "output.json"

try:
    with open(file_path,"r") as file:
        content = json.load(file)
        print(content)
        print(content["name"])
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You dont have permission to read that file")    