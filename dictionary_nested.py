student = {
    "name" : "Rahul",
    "subjects" : {
        "physics" : 97,
        "maths" : 100,
        "chemistry" : 91
    }

}
print(student)
print("\n")
print(student["subjects"])
print("\n")
print(student["subjects"]["maths"])


# keys method
print("\n")
print(student.keys())

print(list(student.keys()))

print(len(list(student.keys())))
print(len(student))


#values method
print("\n")
print(student.values())

print(list(student.values()))

print(len(list(student.values())))
print(len(student))


#items method
print(student.items())
print(list(student.items()))

print("\n")

pairs = list(student.items())
print(pairs[1])


#get method
print("\n")
print("\n")
print(student["name"])              # if not present will give error
print(student.get("name"))          #if not present this method way of will not give error it will return null value
# if error comes lines below will not be executed

#UPDATE METHOD

student.update({"city":"Noida"})
print(student)

print("\n")
print("\n")
new_dict = {"state": "Uttar Pradesh"}
student.update(new_dict)
print(student)

