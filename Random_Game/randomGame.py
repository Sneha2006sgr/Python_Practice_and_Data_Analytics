import random
num=random.randint(1,100)
print("Welcome to number guessing game")

i=0
while True:
    guess=int(int(input("Guess the generated number ")))
    i+=1
    if (guess==num) and(i<=2):
        print(f"You guessed it correct in {i} attempts")
        break
    elif (guess<num)and(i<=2):
        print("you guessed too low")
    elif(guess>num)and(i<=2):
        print("You guessed too high")
    else:
        print(f"Oops!!! you were unable to get it, The correct number was {num}")
