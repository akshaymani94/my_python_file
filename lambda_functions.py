# lambda function is just another way to make a function  

def add(a,b):
    return a+b

minus = lambda x,y : x-y

# this is same as 
"""
def minus(x,y):
    retrun x-y
"""



print(add(5,3))
print(minus(5,3))