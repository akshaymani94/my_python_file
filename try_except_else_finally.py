f1 = open("demo.txt")

try:
    f = open("dothi.txt")
    # f = open("demo2.txt")

except Exception as e:
    print(e)

else:
    print("This will run only if except is not running")

finally:
    print("Run this anyway...")
    f1.close()


