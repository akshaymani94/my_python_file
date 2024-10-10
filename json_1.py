# java script object notation
# like dictionary only

import json

data = '{"var1":"harry","var2":56}'
print(data)
print(type(data))

parsed = json.loads(data)
print(parsed)
print(type(parsed))
print(parsed['var1'])

data2 = {
    "channel_name":"code_with_harry",
    "cars":['bmw','audi','ferrari'],
    "fridge":('roti',540),
    "isbad":False
}

# we cannot directly use this dictionary in java script 
# False is not compatible with java script it should be false
# to make it compatible for java script we use json.dump

jscomp = json.dumps(data2)
print(jscomp)
