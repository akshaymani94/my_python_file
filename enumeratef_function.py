# marks = [12,56,32,98,12,45,1,4]
# index = 0
# for mark in marks:
#     print(mark)
#     if(index == 3):
#         print("Awesome harry")
#     index += 1

# to do this easily 
marks = [12,56,32,98,12,45,1,4]

for index,mark in enumerate(marks,start=0):
    print(mark)
    if(index == 3):
        print("Awesome harry")

# enumerate is a buit in function that gives the value and index at the same time


