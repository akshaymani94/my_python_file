class Person:
    name = "anonymous"

    # def changeName(self,name):
    #     self.name = name            # this name is not for the class. It is created for the instance or the object
    #     # Person.name = name                  # to change for the class use" Person.name = name"
    #     # self.__class__.name = name

    @classmethod
    def changeName(cls,name):       #cls is not self it is actually refering to the class and it is used to directly change the class attributes
        cls.name = name


p1 = Person()
p1.changeName("Rahul kumar")
print(p1.name)
print(Person.name)
