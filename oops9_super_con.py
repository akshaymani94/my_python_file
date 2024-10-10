class A:
    classvar1 = "I am a class Variable in class A"
    
    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        self.classvar1 = "Instance variable in class A"

class B(A):
    classvar1 = "I am in class B"


a = A()
b = B()

print(b.classvar1)

# first it will seach for instance variable first in B and then in A. THen it will se
# search for class variables first in B then in A
