def show(n):
    if(n==0):       # base case is very imp. Orelse we will go into an infinite loop
        return
    print(n)
    show(n-1)
    print("END")

show(5)    # I want to print 5 4 3 2 1 with just one function call

# All the remaining jobs will be done at the end