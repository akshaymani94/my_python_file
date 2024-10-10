
# dict1 = {0:"item0",1:"item1"} ......

dict1 = {i:f"item{i}" for i in range (50) if i%10==0}
print(dict1)

# how to reverse key value pair of dcitionary

dict1 = {value:key for key,value in dict1.items()}
print(dict1)
