import random
import string

print(string.ascii_letters)
print(string.digits)
print(string.punctuation)

charValues = string.ascii_letters+string.digits+string.punctuation


pass_len = 12
password = ""
# for i in range(pass_len):
#     password += random.choice(charValues)

# same thing using list comprehension
password = "".join([random.choice(charValues) for i in range(pass_len)])


print("Your password is :")
print(password)


