numbers = ["3","34","64"]

for i in range(len(numbers)):
    numbers[i] = int (numbers[i])

print(numbers)
numbers[2] = numbers[2] + 1
print(numbers[2])

# to do this without running a loop we use map function

num = ["3","34","64"]
num = list(map(int,num))          #map returns an object we need to convert it into a list
print(num)


def sq(a):
    return a*a

a = [2,3,5,6,7,9]
a = list(map(sq,a))
print(a)

# we can do this using a lambda function also



b = [10,11,12,13,14,15]
b = list(map(lambda x:x*x,b))
print(b)