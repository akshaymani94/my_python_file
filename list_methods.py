marks = [2,1,3]
marks.append(6)

print(marks)
print(marks.sort())    # no output because this function is not returning anything
marks.sort()
print(marks)

marks.sort(reverse=True)
print(marks)

fruits = ["banana","lichi","mango","apple" ]
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)

num = ['c','a','e','b','d']
num.reverse()
print(num)


num = ['c','a','e','b','d']
num.insert(3,'z')
print(num)

num = [2,1,3,1]
num.remove(1)       # first occurance of the number will be removed
print(num)

num = [2,4,3,1]
num.pop(2)
print(num)          # removes element from 2nd index
