class Employee:
    no_of_leaves = 8     
    var = 9
    _protec = 10        # protected: can be accessed by inherited class. Cannot be used by outside class.
    __priva = 98        # became private
    
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
    
emp = Employee("Harry",343,"Programmer")
print(emp._protec)
# print(emp.__priva)      # cannot be accessed like this
print(emp._Employee__priva)         # python did name mangling so that it wont be used outside the class unknowingly
