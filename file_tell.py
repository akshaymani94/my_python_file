# to understand where in the file the pointer is

f = open("akshay2.txt")
print(f.tell())         # tells where the file pointer is
print(f.readline())
print(f.tell())
print(f.readline())
print(f.tell())
print(f.readline())
print(f.tell())

f.close()