import random

highest = 10
answer = random.randint(1, highest)

print("Please guess number between 1 and {}: ".format(highest))
while True:
    guess = int(input())
    if guess == 0:
        print("You Quit The Game Come Back Later!")
        break
    elif guess > answer:
        print("Please enter the lower number")
    elif guess < answer:
        print("Please enter the higher number")
    else:
        print("Well Done Your Guess Is Correct")
        break
