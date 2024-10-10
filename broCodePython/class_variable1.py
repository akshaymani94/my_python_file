class Student:
    
    class_year = 2024           # class variables
    num_students = 0

    def __init__(self,name,age):
        self.name = name                # insatnce variables
        self.age = age

        Student.num_students += 1

student1 = Student("AK",29)
student2 = Student("BK",39)
student3 = Student("CK",49)

print(student1.name)
print(Student.class_year)       # good practice 
print(student2.class_year)

print(Student.num_students) 

print(f"My graduating class of {Student.class_year} has {Student.num_students} students.")
print(student1.name)
print(student2.name)
print(student3.name)

