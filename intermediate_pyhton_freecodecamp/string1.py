from timeit import default_timer as timer
my_list = ['a']*100000

# bad  practice because string is immutable

start = timer()
my_string = ''
for i in my_list:
    my_string += i
stop = timer()
print(f"Time taken by bad practice = {stop-start}")

# good practice
start = timer()
my_string = ''.join(my_list)
stop = timer()
print(f"Time taken by good practice = {stop -start}")
