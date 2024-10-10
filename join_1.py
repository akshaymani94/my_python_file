lis = ["Sachin","Rohit","Kohli","Sanju"]

for item in lis:
    print(item,"and",end = " ")

print("the rest. ")

a = " and ".join(lis)
print(a)