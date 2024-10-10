f = open("akshay.txt","rt")
print(f.readline())
print(f.readline())
f.close()

f = open("akshay.txt","rt")
print("\n")
print(f.readlines())