# def a_first(a):
#     return a[1]


# a = [[1,14],[5,6],[8,23]]        #list of list
# a.sort(key=a_first)
# print(a)


# same thing using a lambda function

a = [[1,14],[5,6],[8,23]]        #list of list
a.sort(key=lambda x:x[1])
print(a)