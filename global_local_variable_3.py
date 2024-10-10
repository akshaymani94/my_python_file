def harry():
    x = 20
    def rohan():
        global x
        x = 88
    print("Before calling rohan()",x)
    rohan()
    print("After calling rohan()",x)
harry()
print(x)