light = input("light : ")

if(light == "red"):
    print("stop")
elif(light == "yellow"):
    print("look")
elif(light == "green"):
    print("go")
else:
    print("light is broken")

marks = int(input("marks : "))
if(marks>=90):
    print("A")
elif(marks>=80 and marks<90):
    print("B")
else:
    print("Need improvement")
