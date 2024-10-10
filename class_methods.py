# methods are functions which belong to the objects
class Student:
    college_name = "Apna College"     


    def __init__(self,name,marks):
        self.name = name                
        self.marks = marks
        
    def welcome(self):
        print("Welcome student")

    def get_marks(self):
        return self.marks


s1 = Student("Karan",97)
s1.welcome()

print(s1.get_marks())






