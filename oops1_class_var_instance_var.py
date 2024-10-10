class Employee:
    no_of_leaves = 8        # cass variable
    pass

harry = Employee()
rohan = Employee()

harry.name = "Harry"
harry.salary = 455
harry.role = "Instructor"

rohan.name = "Rohan"
rohan.salary = 125
rohan.role = "Student"

print(harry.salary) 
print(rohan.role)
print(harry.no_of_leaves)
print(rohan.no_of_leaves)
print(Employee.no_of_leaves)

Employee.no_of_leaves = 18
print(rohan.no_of_leaves)

print(rohan.__dict__)

rohan.no_of_leaves = 20
print(rohan.no_of_leaves)
print(Employee.no_of_leaves)

print(rohan.__dict__)

print(Employee.__dict__)

