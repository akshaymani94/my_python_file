# without multithreading

import threading
import time

# indicates some task is being done
initial = time.perf_counter()


def func(seconds):
    print(f"Sleeping for {seconds} seconds" )
    time.sleep(seconds)

func(4)
func(2)
func(1)
final = time.perf_counter()

print(f"Total time taken = {final-initial}")