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
    

class Programmer(Employee):
    def __init__(self,aname,asalary,arole,langauges): 
        super().__init__(aname,asalary,arole)
        self.langauges = langauges


    def printprog(self):
        return f"The programmers name is {self.name}. Salary is {self.salary} and role is {self.role}. The languages are {self.langauges}"


    


harry = Employee("Harry",455,"Instructor")
rohan = Employee("Rohan",125,"Student")



shubam = Programmer("Shubam",555,"Programmer",["Python"])
karan = Programmer("Karan",777,"Programmer",["Python","C++"])
print(karan.printprog())
print(shubam.printprog())
print(karan.printdetails())
