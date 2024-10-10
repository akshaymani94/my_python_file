
# STAIC METHOD belongs to the class rather than any object created from the class.
# It is best for utility function that does not need any class data
class Employee:

    def __init__(self,name,position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name}={self.position}"
    
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["CFD Engieer","CSE","Python developer"]
        return position in valid_positions
    

employee1 = Employee("Akshay","CFD Engineer")
employee2 = Employee("Dp","CSE")
employee3 = Employee("Akk","Python Developer")

print(Employee.is_valid_position("Scientist"))
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())
