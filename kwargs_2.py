def funargs(normal,*args,**kwargs):             #*args can also be name *akshay also
    print(args[2])
    print(type(args))
    for item in args:
        print(item)
    print(normal)
    print("\nNow let let us introduce our heros")
    for key,value in kwargs.items():
        print(f"{key} is the {value}")


name = ["harry","roshan","mathew","shoaib"]     # even if I add a new name there wont be any issue
normal_arg = "This is a normal argument"
kw = {"Akshay":"CEO","Karthi":"CTO","Amruth":"CFO","Kirthi":"HR"}


funargs(normal_arg,*name,**kw)

