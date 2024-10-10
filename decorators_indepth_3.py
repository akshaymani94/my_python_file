def greet(fx):
    def mfx(*args,**kwargs):
        print("Good morning")
        fx(*args,**kwargs)
        print("Thanks for using this function")
    return mfx


@greet
def add(a,b):
    print(a+b)

add(5,6)
# greet(add)(5,6)

