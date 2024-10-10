try:
    i = int(input("Enter a number : "))
    c = 1/i
except Exception as e:
    print(e)
    exit()

finally:                    # will be done irrespective of exception
    print("We are done")

print("Thanks for using he program")        # this willnnot get printed if exception is raised