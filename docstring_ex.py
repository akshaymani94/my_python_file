def square(num):
    '''This functions returns the 
        square of the given number'''
    return num*num

ans=square(5)
print(ans)
print(square.__doc__)

# doc string should be written right below the function name or write above the function body
# if not it will not be considered as a docstring
