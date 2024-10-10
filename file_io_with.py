

with open("akshay2.txt") as f:
   a =  f.read(4)
   print(a)


# we do not read close file explicitly in this case
# therefore idf we try to read the function outside the with lock we wont be able to
