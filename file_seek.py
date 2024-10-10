f = open("akshay2.txt")      
print(f.readline())
f.seek(0)                   # tells the pointer to go to line 
print(f.readline())
f.seek(0)
print(f.readline())

f.close()