def check_for_line():
    word = "learning"
    data = True
    line_no = 1
    with open("practice.txt","r") as f:
        while data:
            data = f.readline()
            if(data.find(word)!=-1):
                print(line_no)
                return
            line_no += 1

    return -1 

print(check_for_line())


    