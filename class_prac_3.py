class Circle:
    def __init__(self,radius):
        self.radius = radius
        print("Circle created")
    def area_circle(self):
        area = (22/7)*(self.radius)**2
        return area
    def peri_circle(self):
        peri = 2*(22/7)*self.radius
        return peri

c1 = Circle(21)
print("Area of circle",c1.area_circle())
print("Perimeter of circle",c1.peri_circle())

