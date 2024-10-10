sub = {}
sub.update({"Maths ":input("Maths")})
sub.update({"Physics ":input("Physics")})
sub.update({"Chemistry ":input("Chemistry")})
print(sub)

marks = {}

x = int(input("Enter Physics : "))
marks.update({"Physics":x})
x = int(input("Enter Math : "))
marks.update({"Math":x})
x = int(input("Enter Chemistry : "))
marks.update({"Chemistry":x})
print(marks)
