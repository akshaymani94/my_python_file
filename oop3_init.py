class Employee:
    no_of_leaves = 8        
    
    def __init__(self,aname,asalary,arole):         # will be doone automaticallly at the time of object creation
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"

harry = Employee("Harry",455,"Instructor")
rohan = Employee("Rohan",125,"Student")


# harry.name = "Harry"
# harry.salary = 455
# harry.role = "Instructor"

# rohan.name = "Rohan"
# rohan.salary = 125
# rohan.role = "Student"

print(rohan.printdetails())