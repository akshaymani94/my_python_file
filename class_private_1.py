class Person:
    __name = "anonymous"

    def __hello(self):
        print("hello")

    def welcome(self):
        self.__hello()
    
p1 = Person()

# print(p1.__name)
# print(p1.__hello)
p1.welcome()