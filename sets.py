collection = {1,2,3,4,"hello","world",1,4}     # duplicate items are not alloowed inside sets
print(collection)
print(type(collection))

collection1 = {}   # this is syntax of empty dictionary
print(type(collection1))

# to create empty set the syntax used is

collection2 = set()         # syntax for declaring empty dictionary
print(type(collection2))
 
collection2.add(1)
collection2.add(2)
collection2.add(2)      # our set will igmore duplicae values
collection2.add("Akshay")    


print(collection2)


collection2.remove(1)
print(collection2)

collection2.add((98,99,100))
print(collection2)

# collection2.add([101,109,111])        will throw an error because list is mutable  
print(collection2)
print(len(collection2))

collection2.clear()
print(len(collection2))

collection3 = {"Hi","I","am","the","best"}
print(collection3.pop())        # randomly picks any value
print(collection3.pop())

# union and intersection

set1 = {1,2,3}
set2 = {3,4,5}


print(set1)
print(set2)
print(set1.union(set2))
print(set1.intersection(set2))






