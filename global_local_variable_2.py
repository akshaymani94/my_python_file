# to change global variable

l=10            # global

def function1(n):
    global l         
    l = 154
    print(n,"I have printed")
    print(l)

function1("This is me")
print(l)

