import random
num = random.randint(1,100)
while True:
    print("Guess a number between 1 and 100")
    guess=int(input())
    if guess == num:
        print("You guessed right! Bingo.")
        break
    elif guess < num :
        print("Try a higher value.")
    elif guess > num :
        print("Guess a lower value")
    else:
        print("Try again and again")

