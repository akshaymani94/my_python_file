class Employee:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@codewithharry.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"
    
    @property
    def email(self):
        return f"{self.fname}.{self.lname}@codewithharry.com"
    
    @email.setter
    def email(self,string):
        print("Setting now...")
        names = string.split("@")[0]
        self.fname =names.split(".")[0]
        self.lname =names.split(".")[1]

skillf = Employee("Skill","f")
print(skillf.email)

print(type(skillf))

print(type("I am the best"))
print(id("I am the best"))
print(id("I am the best"))
print(id("I am Akshay"))

o = "I am Akshay"
print(dir(o))       # will give all methods whcih are defined under this

print("\n\n\n")
print(dir(skillf))

print("\n")
import inspect
print(inspect.getmembers(skillf))