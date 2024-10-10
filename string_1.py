mystr = "My name is akshay"
print(mystr[4])
print(mystr[0:4])
print(len(mystr))
print(mystr[0:18:2])
print(mystr[0:])
print(mystr[:])
print(mystr[::])
print(mystr[:2])

print(mystr.find("is"))
print(mystr.lower())
print(mystr.upper())

print(mystr.replace("is","are"))



# negavtive indices

str = "abcdefghijklmnopqrstuvwxyz"
print(str)
print(len(str))
print(str[-4:-2])
print(str[::-1])        # reverses the string
print(str[::-2])

str1 = "abcdefghijklmnopqrstuvwxyz"
print(str1.isalnum())
print(str1.isalpha())
print(str1.endswith("z"))
print(str1.capitalize())


str2 = "abcdefg hijklmnop qrstuvwx yz"
print(str2.isalnum())
print(str2.isalpha())
print(str2.count("a"))

