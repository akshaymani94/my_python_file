import threading
import time

# indicates some task is being done
initial = time.perf_counter()

def func(seconds):
    print(f"Sleeping for {seconds} seconds" )
    time.sleep(seconds)

# func(4)
# func(2)
# func(1)


# we can do this all at once. This can be done using multithreadng

t1= threading.Thread(target=func,args=[4])
t2= threading.Thread(target=func,args=[2])
t3= threading.Thread(target=func,args=[1])

t1.start()
t2.start()
t3.start()

t1.join()       # I will wait till t1 is over
t2.join()       # I will wait till t2 is over
t3.join()       # I will wait till t3 is over



final = time.perf_counter()

print(f"Total time taken = {final-initial}")