class Employee:
    no_of_leaves = 8        
    
    def __init__(self,aname,asalary,arole):         # will be doone automaticallly at the time of object creation
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves = newleaves



harry = Employee("Harry",455,"Instructor")
rohan = Employee("Rohan",125,"Student")



print(rohan.printdetails())
Employee.no_of_leaves = 10
print(harry.no_of_leaves)


harry.change_leaves(34)         # will change for the netire class. Will not take self as an argument

print(harry.no_of_leaves)
print(rohan.no_of_leaves)
print(Employee.no_of_leaves)