from datetime import datetime
def getdate():
    current_date = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    return current_date

def log():
    print("For whome do you want log data for : ")
    realname = int(input("1 : Harry 2 : Rohit 3 : Kavya "))
    if realname == 1:
        f = open("Harrylog.txt","w")

        data1 = getdate()
        print(type(data1))
        data = input("Enter what you ate : ")
        data2 = getdate()
        f.write(data2+"  :  "+data+"\n")

        f.close()
        print("Writtern successfully")       
    elif realname == 2:
        f = open("Rohitlog.txt","a")
        data1 = getdate()
        print(type(data1))
        data = input("Enter what you ate : ")
        data2 = getdate()
        f.write(data2+"  :  "+data+"\n")



        f.close()
        print("Writtern successfully")
    elif realname == 3:
        f = open("Kavyalog.txt","a")
        data1 = getdate()
        print(type(data1))
        data = input("Enter what you ate : ")
        data2 = getdate()
        f.write(data2+"  :  "+data+"\n")


        f.close()
        print("Writtern successfully")

def retrieve():
    print("For whome do you want to retrieve data for : ")
    realname = int(input("1 : Harry 2 : Rohit 3 : Kavya"))
    if realname == 1:
        fr = open("Harrylog.txt","r")
        lines = fr.readlines()
        for line in lines:
            print(line)
        fr.close()
    elif realname == 2:
        fr = open("Rohitlog.txt","r")
        lines = fr.readlines()
        for line in lines:
            print(line)
        fr.close()
    elif realname == 3:
        fr = open("Kavyalog.txt","r")
        lines = fr.readlines()
        for line in lines:
            print(line)
        fr.close()
    
    
    

print("Do you want to log or retrieve data : ")
enname = input("Input 'l' for log and 'r' for retrieve : ")
if enname == 'l':
    log()
else:
    retrieve()
