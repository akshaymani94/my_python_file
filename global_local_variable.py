l=10            # global

def function1(n):
    l=5         # local
    m=8
    print(n,"I have printed")
    print(l)

function1("This is me")
print(l)
# print(m)      #error
