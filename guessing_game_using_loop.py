import random
number = random.randint(1, 10)
print("welcome to number guessing game")
print("you have to guess the number which i selected")


for n in range(1,11):
    n=int(input("guess a number between 1 to 10:"))
    if n<number:
        print("Too low,try again")
    elif n>number:
        print("Too high,try again")
    else:
        print("congratulations!! you won the game")
        break

print("My number is",number)




