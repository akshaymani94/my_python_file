import pickle

file = "mycar.pkl"
fileobj = open(file,'rb')       # read binary
mycar = pickle.load(fileobj)
print(mycar)
print(type(mycar))


