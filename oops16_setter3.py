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
    
hindustani_supporter = Employee("Hindustani","Supporter")
nikhil_raj_pandey = Employee("Nikhil","Raj")

print(hindustani_supporter.email)

hindustani_supporter.fname = "us"

print(hindustani_supporter.email)      # we can use it as a property not a function email()
# nopw we cannot use it as a function becasuse we have used a decorator

# hindustani_supporter.email = "this.that@codewithharry.com"      # we cannot do this for this we will have to use a setter