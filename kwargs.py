# function cannot change the number of arguments it takes in inbetween the programme

def funargs(normal,*args,**kwargs):             #*args can also be name *akshay also
    print(args[2])
    print(type(args))
    for item in args:
        print(item)
    print(normal)


name = ["harry","roshan","mathew","shoaib"]     # even if I add a new name there wont be any issue
normal_arg = "This is a normal argument"
funargs(normal_arg,*name)

# normal arguments should be always given first
# if you give normal argument next then it will throw an error

# order of writing arguments
# normal,args,kwargs

# if you give or dont give args and kwargs it is not an issue