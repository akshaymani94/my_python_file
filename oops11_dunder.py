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
        return self.salary + other.salary           # Internally calls obj1.__add__(obj2)
    
    def __truediv__(self,other):
        return 756


emp1 = Employee("Harry",455,"Programmer")
emp2 = Employee("Rohan",45,"Cleaner")


print(emp1+emp2)        # Internally calls obj1.__add__(obj2)
print(emp1/emp2)