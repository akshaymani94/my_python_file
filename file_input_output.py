f = open("demo.txt","r")        # if file is not in same folder we will have rto type the complete path /home/mechfoam/python/demo.txt
data = f.read()
print(data)
print(type(data))

f.close()

print("\n")
f = open("demo.txt","r")        # if file is not in same folder we will have rto type the complete path /home/mechfoam/python/demo.txt
data = f.read(5)                # reads ony 5 characters
print(data)
print(type(data))

f.close()

print("\n")
f = open("demo.txt","r")        
line1 = f.readline()
print(line1)
print(type(line1))

f.close()


print("\n")
f = open("demo.txt","r")        
line1 = f.readline()
print(line1)
line2 = f.readline()
print(line2)


f.close()



print("\n")
f = open("demo.txt","r") 
data = f.read()
print(data)       
line1 = f.readline()
print(line1)
line2 = f.readline()
print(line2)


f.close()