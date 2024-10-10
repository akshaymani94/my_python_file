# i want a fucntion which will do anything but before doing that it has
# do something specified and also do something specified after running the programm
# decorators modify a function

def greet(fx):
    def mfx():
        print("Good morning")
        fx()
        print("Thanks for using this function")
    return mfx


# @greet
def hello():
    print("Hello world")

# hello()
greet(hello)()