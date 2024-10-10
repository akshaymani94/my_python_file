# use paranthesis for generator comprehension
evens = (i for i in range(100) if i%2 == 0)
print(type(evens))
print(evens.__next__())
print(evens.__next__())
print(evens.__next__())

