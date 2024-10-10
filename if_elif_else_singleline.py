food = input("food: ")
eat = "Yes" if food == "cake" else "No"
print(eat)

food = input("food: ")
print("sweet") if food == "cake" or food == "jalebi" else print("Not sweet")

age = int(input("age : "))
vote = ("can vote","cannot vote")[age<18]
print(vote)
