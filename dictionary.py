info = {
    "name" : "Akshay",
    "learning" : ["CFD","C++","Bash","Machine Learning"],
    "skills" : ("Decipline","Ethics"),
    "age" : 29,
    "gender" : "male",
    "is_adult" : True,
    "Score" : 79.83,
    12.56 : "Twelve point five six",
    False : "Am I a lier"

}

# keys can be int,float, string, tuple, bool but cannot be list
# ie something which cannot be changed
# tuple is immutable therefore it can be used as key

#unordered
#string list and tuple has index therefor there is order
#Dictionary is mutable
#Key cannot be duplicate

print(info)
print(type(info))


# to acces an elelment

print(info["Score"])
print(info["learning"])

info["name"] = "Dpk"
info["surname"] = "C"
print(info)

null_dict = {}
print(null_dict)

