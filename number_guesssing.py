import random as rd
a = rd.randint(1,100)
print(a)

print("Guess the number")
while (True):
    b  = input("Enter your guess or Quit (Q) : ")
    if(b == "Q"):
        break
    b = int(b)
    if (b == a):
        print("Correct Guess")
        break
    elif (b < a):
        print("Number is greater than your guess")
    else :
        print("Number is less than your guess")

print("----GAME OVER----")