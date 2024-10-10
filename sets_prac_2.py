values = {9,9.0,8,8.25}     # hash of 9 and 9.0 are same
print(values)

values1 = {9,"9.0",8,8.25}  
print(values1)

values2 = {
    ("float",9.0),              # forming pairs in the form of tuple
    ("int",9)
}
print(values2)