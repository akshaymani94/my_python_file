import os

print(dir(os))
print(os.getcwd())

# if you want to change your working directory

os.chdir("/home/mechfoam/qt")
print(os.getcwd())
os.chdir("/home/mechfoam/python")
print(os.getcwd())

print(os.listdir())
# os.mkdir("This")        # to create new folder
# os.makedirs("that/in")  # to make directories
# os.rename("akshay.txt","akshaypython.txt")

print(os.environ.get('Path'))       # prints the set envoironment variables
print(os.path.exists("/home/mechfoam/qt"))
print(os.path.isfile("/home/mechfoam/qt"))
print(os.path.isdir("/home/mechfoam/qt"))


