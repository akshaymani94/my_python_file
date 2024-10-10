with open("practice2.txt","r") as f:
    data = f.read()

# we want to replace all occurance of java with python
# data is a string therefore we can use replace method

new_data=data.replace("Java","Python")
print(new_data)

with open("practice2.txt","w") as f:
    f.write(new_data)