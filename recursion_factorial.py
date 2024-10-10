def fact(n):
    if(n == 0 or n == 1):           # base case . This is very important
        return 1
    else:
        return n*fact(n-1)
    
print(fact(6))