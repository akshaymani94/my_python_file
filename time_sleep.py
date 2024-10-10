import time

initial = time.time()

k=0
while(k<45):
    print("Akshay")
    time.sleep(2.0)
    k += 1

print(f"While loop ran in {time.time()-initial}")