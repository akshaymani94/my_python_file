# how to handle error gracefully or else it will interrupt our programm

try:
    number = int(input("Enter a number : "))
    print(1/number)

except ZeroDivisionError:
    print("You cant divide by zero")

except ValueError:
    print("Enter only numbers")

finally:        # will get executed regardles of there is exception or not
    print("Thank you")


