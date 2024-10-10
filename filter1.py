lis = [1,2,3,4,5,6,7,8,9]

def is_greater_5(num):
    return num>5

print(is_greater_5(6))

gr_than_5 = list(filter(is_greater_5,lis))
print(gr_than_5)