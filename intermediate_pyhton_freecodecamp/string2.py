# formating string
var = "Tom"
my_string = "the variable is %s" %var
print(my_string)

var = 8
my_string = "the variable is %d" %var
print(my_string)

var = 3.6865
my_string = "the variable is %f" %var
print(my_string)

var = 3.6865
my_string = "the variable is %.2f" %var
print(my_string)

# new formating method
var = 3.6865655
my_string = "the variable is {}" .format(var)
print(my_string)

var = 3.6865655
my_string = "the variable is {:.2f}" .format(var)
print(my_string)

var = 3.6865655
var2 = 6
my_string = "the variable is {:.2f} {}" .format(var,var2)
print(my_string)

# newest method is fstrings
var = 3.6865655
var2 = 6
my_string = f"the variable is {var} {var2}"
print(my_string)
