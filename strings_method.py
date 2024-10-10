str1 = 'This is a "string"'
str2 = "Akshay's skill"
print(str1)
print(str2)

str3 = "This is a string \n created in python"
print(str3)

str4 = "My name"
str5 = "is __"
str6 = str4+" "+str5
print(str6)

print(len(str6))
print(str4[1])


#slicing
str7 = "abcdefghij"
print(len(str7))
print(str7[4:7])        #slicing
print(str7[4:10])  
print(str7[4:len(str7)])        
print(str7[4:])  

#negative indexing
str8 = "apple"
print(str8[-3:-1])


#string functions
str9 = "abcdefghij"
print(str9.endswith("ij"))
print(str9.capitalize())    # capitalises first character
print(str9)

print(str9.replace("a","o"))   # replaces a with o

str10 = "I am working as a CFD Engineer with an Engineer"
print(str10.find("CFD"))        # GIVES INDEX OF FIRST OCCURANCE
print(str10.find("am"))   
print(str10.find("q"))   
print(str10.count("Engineer"))




