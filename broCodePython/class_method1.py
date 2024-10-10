# CLASS METHODS :  BEST USED WHEN WE ARE WORKING WITH CLASS LEVEL DATA
# or requires access to class itself

class Student:

    count = 0
    total_gpa = 0

    def __init__(self,name,gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    def get_info(self):
        return f"{self.name}   {self.gpa}"
    
    @classmethod
    def get_count(cls):
        return f"The total number of Students = {cls.count}"
    
    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average GPA : {cls.total_gpa / cls.count:.2f}"

student1 = Student("AK",9.8)
student2 = Student("BK",7.8)
student3 = Student("CK",5.8)


print(Student.get_count())
print(Student.get_average_gpa())

