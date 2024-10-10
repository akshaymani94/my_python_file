class Student:
    def __init__(self,fullname):             # self will alwaays be first parameter
        print(self)                         # it need not be named self it can be also named 'abcd'
        self.name = fullname
        print("Adding new student in data base ...")

s1 = Student("Karan")
print(s1)               # self is telling about s1 object only
print(s1.name)

s2 = Student("Arjun")
print(s2)
print(s2.name)