class Student:
    college_name = "Apna College"       # class attribute
    name = "Anonymous"

    def __init__(self,name,marks):
        self.name = name                # object attribute
        self.marks = marks
        print("Adding new Student in the database..")

s1 = Student("Karan",97)
s2 = Student("Arjun",78)

print(s1.name)          # if we have same name for class attributes and object attributs then precedence will be higher for object attributes
print(s1.marks)
print(s1.college_name)
print(Student.college_name)

print(s2.name)
print(s2.marks)
print(s2.college_name)
print(Student.college_name)


