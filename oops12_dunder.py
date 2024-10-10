class Employee:
    no_of_leaves = 8        
    
    def __init__(self,aname,asalary,arole):       #dunder init  
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves = newleaves

    def __add__(self,other):                        #operator overloading
        return self.salary + other.salary
    
    def __truediv__(self,other):
        return 756

    def __repr__(self):
        return f"Employee {(self.name), (self.salary), (self.role)}"
    
    def __str__(self):
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"


emp1 = Employee("Harry",455,"Programmer")

print(emp1)         # preferece is for str method
print(str(emp1))        # when ever str is present preferecne is given for str
print(repr(emp1))
