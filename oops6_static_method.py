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


# easier method
    @classmethod
    def from_dash(cls,string):
        return cls(*string.split("-"))
    

    @staticmethod
    def printgood(str):
        return "This is good "+ str

    


harry = Employee("Harry",455,"Instructor")
rohan = Employee("Rohan",125,"Student")

karan = Employee.from_dash("Karan-480-student")

print(karan.salary)

print(karan.printgood("Akshay"))
