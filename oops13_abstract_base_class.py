from abc import ABCMeta, abstractmethod

class Shape(metaclass = ABCMeta):
    @abstractmethod
    def printarea(self):
        return 
    
# ABC Meta class tells the classes that inherit from it hat it has to imopleiment some methods what ever it is if you are inheriting from me
    
class Rectangle(Shape):
    type = "Rectangle"
    sides = 4

    def __init__(self):
        self.length = 6
        self.breadth = 7

    def printarea(self):
        return self.length * self.breadth

rect1 = Rectangle()
print(rect1.printarea())

# tryobj = Shape()        # we cannot create objects for abstract base class