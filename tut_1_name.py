def printak(str):
    return f"This is {str}"

def addnum(num1,num2):
    return num1+num2+5

print(f"The name is {__name__}")

if __name__ == '__main__':          # if this was not there then the complete program would be executed 
    print(printak("Akshay!"))       # once you import tut_1_name. To prevent this we write __name__ =='__main__' , this
    o = addnum(4,6)                 # is like the main function in cpp
    print(o)                        # this is helpful if you want to use same functions in multiple programs


# the value of name will be main only when we are in the same program and running it. It wont be main if we are running from some other program
# there fore we are asking to check if the value of name is main, if it is not then dont execute what is coming below    