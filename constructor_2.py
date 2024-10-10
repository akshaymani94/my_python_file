class Student:

# default constructor
    def __init__(self):
        pass 

# parameterized constructor
    def __init__(self,name,marks):             # self will alwaays be first parameter
        print(self)                         # it need not be named self it can be also named 'abcd'
        self.name = name
        self.marks = marks  
        print("Adding new student in data base ...")

s1 = Student("Karan",98)
print(s1)               # self is telling about s1 object only
print(s1.name)
print(s1.marks)

s2 = Student("Arjun",87)
print(s2)
print(s2.name)
print(s2.marks)