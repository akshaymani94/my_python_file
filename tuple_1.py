marks = (2,1,3,1)
print(type(marks))
print(marks[2])

# marks[0]=4        Not possible because tuples are immutable

num =()         #empty tuple
num2 = (1,)      # initializing tuple with a single value

print(type(num))
print(type(num2))

num3 = (1)              # if we dont put a comma it will be considered as an int
print(type(num3))

name = ("hello",)
print(type(name))

num4 = (1,2,3,4,)
num5 = (1,2,3,4)
print(type(num4))
print(type(num5))


# slicing in tuples
print(num4[1:3])

