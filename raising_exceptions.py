def increment(num):
    try:
        return int(num)+1
    except:
        raise ValueError("This is not good - Akshay")
    
a = increment('table')
print(a)