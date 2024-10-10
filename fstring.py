import math

me = "harry"
a1 = 3
a = "This is %s %s"%(me,a1)
print(a)

# or

b = "This is {} {}"
c = b.format(me,a1)
print(c)

b = "This is {1} {0}"
d = b.format(me,a1)
print(d)


# fstring   readability will also be better
e = f"this is {me} {a1} {4*12} {math.cos(65)}"
print(e)


