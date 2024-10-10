# function cannot change the number of arguments it takes in inbetween the programme

def funargs(*args):             #*args can also be name *akshay also
    print(args[2])
    print(type(args))
    for item in args:
        print(item)


name = ["harry","roshan","mathew","shoaib"]     # even if I add a new name there wont be any issue
funargs(*name)

