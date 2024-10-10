import pickle

# pickling a python object and storing it in a file as it is

cars = ["Audi","BMW","Maruti","Benz"]
file = "mycar.pkl"
fileobj = open(file,'wb')
pickle.dump(cars,fileobj)
fileobj.close()
