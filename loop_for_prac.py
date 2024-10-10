nums = [1,2,3,4,5,6,7,8,9,10]
for i in nums:
    print(i*i)

x = 7
idx = 0
for i in nums:
    if (i==x):
        print("Number found at index : ",idx)
    idx += 1

