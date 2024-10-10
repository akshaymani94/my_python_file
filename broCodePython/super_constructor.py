class Shape:
    def __init__(self,color,is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape):
    def __init__(self,color,is_filled,radius):
        super().__init__(color,is_filled)
        self.radius = radius

    def describe(self):
        print(f"It is a circle with an area of {3.14*self.radius*self.radius} cm2")
        super().describe()

class Square(Shape):
    def __init__(self,color,is_filled,width):
        super().__init__(color,is_filled)
        self.width = width

class Triangle(Shape):
    def __init__(self,color,is_filled,width,height):
        super().__init__(color,is_filled)
        self.width = width
        self.height = height

circle = Circle(color="red",is_filled=True,radius=5)
square = Square(color="blue",is_filled=False,width=6)
triangle = Triangle(color="yellow",is_filled=True,width=7,height=8)

print(circle.color)
print(circle.is_filled)        
print(circle.radius)
print(square.color)
print(square.is_filled)
print(square.width)
print(triangle.color)
print(triangle.is_filled)
print(triangle.width)
print(triangle.height)

circle.describe()        # if a child uses the same method as the parent we will use the method of the child. This is called method overriding
square.describe()
triangle.describe()