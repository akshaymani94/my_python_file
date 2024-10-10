marks1 = 94.4
marks2 = 87.5
marks3 = 95.2
marks4 = 66.4
marks5 = 45.1

marks = [94.4,87.5,95.2,66.4,45.1]
print(marks)
print(type(marks))
print(marks[1])
print(len(marks))

student = ["Akshay",29,"Noida","India"]
print(student)
print(type(student))    
print(student[2])
print(len(student))

student[2]="Delhi"          # lists are mutable
print(student)

#slicing in lists
print(student[1:3])
print(marks[1:4])
print(marks[:4])
print(marks[2:])

print(marks[-3:-1])
