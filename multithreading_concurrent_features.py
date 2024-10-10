import threading
import time
from  concurrent.futures import ThreadPoolExecutor

initial = time.perf_counter()

def func(seconds):
    print(f"Sleeping for {seconds} seconds" )
    time.sleep(seconds)

def main():
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

def poolingDemo():
    with ThreadPoolExecutor() as executor:
        future1 = executor.submit(func,3)
        future2 = executor.submit(func,2)
        future3 = executor.submit(func,4)
        print(future1.result())
        print(future2.result())
        print(future3.result())

poolingDemo()

