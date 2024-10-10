# decorators

def dec1(func1):
    def nowexec():
        print("Executing now")
        func1()
        print("Executed")
    return nowexec

def who_is_harry():
    print("Harry is a good boy")

who_is_harry = dec1(who_is_harry)
who_is_harry()


