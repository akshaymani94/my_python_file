import file2_import         # this is the better practice
# print(a)        # error
print(file2_import.a)

from file3_import import b
print(b)               # no error
# print(file3_import.b)   #error

import file3_import
file3_import.printjoke("He he he")