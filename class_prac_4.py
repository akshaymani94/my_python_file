class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("Role = ",self.role)
        print("Dept = ",self.dept)
        print("Salary = ",self.salary)


class Engineer(Employee):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        super().__init__("Engineer","IT","75,000")

e1 = Employee("Accountant","finance","60,000")
e1.showDetails()

e2 = Engineer("Elon Musk","40")
e2.showDetails()