"""
Modes for opening a file
"r"  - Open a file for reading  - default mode
"w" - Open a file for writing
"x" - Creates file if not exits
"a" - Adds more content to a file
"t" - text mode -  default mode
"b" - binary mode
"+" - read and write
"""

#f = open("akshay.txt")      # or  f = open("akshay.txt","r")
f = open("akshay.txt","rt")
content = f.read()
print(content)
f.close()

print("\n")

f = open("akshay.txt","rt")
content = f.read(3)
print(content)
f.close()



