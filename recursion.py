def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)

show(5)    # I want to print 5 4 3 2 1 with just one function call