from functools import reduce

lis = [1,2,3,4]

num = 0
for i in lis:
    num = num + i 

print(num)

# easier way to do this

prod = reduce(lambda x,y:x+y, lis)
print(f"Using reduce we got {prod} in one line of code")

