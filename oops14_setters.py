class Employee:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        self.email = f"{fname}.{lname}@codewithharry.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"
    
    def printemail(self):
        pass
    
hindustani_supporter = Employee("Hindustani","Supporter")
nikhil_raj_pandey = Employee("Nikhil","Raj")

print(hindustani_supporter.email)

hindustani_supporter.fname = "us"
print(hindustani_supporter.email)       # will not change because it was set at run time.
# this problem can be solved by setter
