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

    
hindustani_supporter = Employee("Hindustani","Supporter")
nikhil_raj_pandey = Employee("Nikhil","Raj")

print(hindustani_supporter.email)

hindustani_supporter.fname = "us"

print(hindustani_supporter.email)      

hindustani_supporter.email = "this.that@codewithharry.com"
print(hindustani_supporter.fname)
print(hindustani_supporter.lname)
print(hindustani_supporter.email)

del hindustani_supporter.email