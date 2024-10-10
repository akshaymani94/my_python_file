# function can take function as an argument

def executor(func):
    func("This is it")

executor(print)

# function can also retuen function

def funcret(num):
    if num==0:
        return print
    if num==1:
        return int
    
a = funcret(1)
print(a)