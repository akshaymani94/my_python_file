with open("demo2.txt","r") as f:
    data = f.read()
    print(data)

# no need to explicitly cloase with does it for us. SO you dont need to do it manually

with open("demo2.txt","a") as f:
    f.write("\nThis is the newly appended line")
  
with open("demo2.txt","r") as f:
    data = f.read()
    print(data)
