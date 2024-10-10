"""
iterable- __iter__()  or __getit
iterator- __next__()     generators is a type of iterator which you can iterate only once. It is used to save our RAM
iteration- 
"""

def gen(n):
    for i in range(n):
        yield i

# g = gen(6546787167971979)
g = gen(3)
print(g.__next__())
print(g.__next__())
print(g.__next__())

# for i in g:
#     print(i)

h = "harry"
ier = iter(h)
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())


# h = 546546                #    int is not iterable therefore __iter__ and __getit is not defned for it
# ier = iter(h)
# print(ier.__next__())
# print(ier.__next__())
# print(ier.__next__())