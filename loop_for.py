nums = [1,2,3,4,5]                          #list

for val in nums:
    print(val)

veg = ("potato","tomato","brinjal")         #tuple

for val in veg:
    print(val)

str = "Akshay Mani"                         #string

for let in str:
    if (let == 'l'):
        print("Character found")
        break
    print(let)
else:
    print("Not found")                    # WILL NOT get executed unless the loop is fully executed, when break is used it wont get executed

