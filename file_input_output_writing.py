f = open("/home/mechfoam/python/demo.txt","w")
f.write("This is Akshay 722")
f.close()

f = open("/home/mechfoam/python/demo.txt","a")
f.write("\nI am living in Mayur Vihar Phase 3")
f.close()


# if we open file in "w" or "a"  mode and if it doesnt exist then 
# python automatically creates it for us

f = open("sample.txt","w")
f.close()

f = open("sample.txt","w")
f.write("This is a trial to see how r+ anw w+ work")
f.close()

f = open("sample.txt","r+")
f.write("Akshay")                   # over write, pointer at start, no truncation
f.close()

f = open("sample.txt","w+")         #over write and truncation
f.write("What has happened")
f.close()

f = open("sample.txt","a+")
f.write("Am I getting appended or truncated")   #pointer at the end, no truuncation
f.close()