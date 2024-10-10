# decorators are functions that extends the behavior of another function
# without modifying the base function
# Pass the base function as an argument to the decorator function

def add_sprinkles(func):
    def wrapper():
        print("*You add sprinkles*")
        func()
    return wrapper

@add_sprinkles
def get_ice_cream():
    print("Here is your ice cream")

get_ice_cream()
