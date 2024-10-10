# ls  =[]
# for i in range(100):
#     if i%3 == 0:
#         ls.append(i)

# print(ls)

# How to write this in ONE line

ls = [i for i in range(100) if i%3 == 0]        # list comprehesnion
print(ls)