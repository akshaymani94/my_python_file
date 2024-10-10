import time

initial = time.time()

k=0
while(k<45):
    print("Akshay")
    k += 1

print(f"While loop ran in {time.time()-initial}")


initial2 = time.time()
k=0
for i in range(45):
    print("Akshay")

print(f"For loop ran in {time.time()-initial2}")

localtime = time.asctime(time.localtime(time.time()))
print(localtime)