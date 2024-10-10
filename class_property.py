# class Student:
#     def __init__(self,phy,chem,math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math
#         self.percentage = str((self.phy +self.chem + self.math)/3)+"%"

#     def calcPercen  tage(self):
#         self.percentage = str((self.phy +self.chem + self.math)/3)+"%"
        

# stu1 = Student(98,97,99)
# print(stu1.percentage)

# stu1.phy = 86
# print(stu1.phy)
# print(stu1.percentage)
# stu1.calcPercentage()
# print(stu1.percentage)


# better way to do the above is

class Student:
    def __init__(self,phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def percentage(self):
        return str((self.phy +self.chem + self.math)/3)+"%"

stu1 = Student(98,97,99)
print(stu1.percentage)

stu1.phy = 86
print(stu1.phy)
print(stu1.percentage)
            
# now when we change the marks of physics the percentage will also automatically change. we dfont have to amke anither method to do this
# this is because we made it into a property
