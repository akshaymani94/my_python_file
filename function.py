# function definition
def calc_sum(a,b):          #parameters
    sum = a + b
    print(sum)
    return sum


a = 5
b = 10
result = calc_sum(a,b)          # function call, arguments
print("The sum of",a,"and",b,"is",result)

def print_hello():
    print("Hello")

print_hello()
print_hello()
print_hello()
print_hello()
print_hello()

output = print_hello()
print(output)               # not returning any value therefore


