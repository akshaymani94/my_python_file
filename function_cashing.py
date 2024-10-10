from functools import lru_cache
import time

@lru_cache(maxsize=3)
def some_work(n):
    # some task taking n seconds
    time.sleep(n)
    return n
 
print("Now running some work")
print(some_work(5))
print("Calling again")
print(some_work(5))
print("complete")

# we dont want to waste time for doing the same work over and over again
# there fore we ask python to save it.
# This is called cashing
# We can ask python to save last n calls
# we are doing it for latest 3 calls
# we can use lru_cache for this purpose
# it is a decorator


