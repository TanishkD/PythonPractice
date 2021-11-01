import random

userMinimum = int(input("Enter a minimum amount: "))
userMaximum = int(input("Enter a maximum amount: "))
userGuess = int(input("What is your guess? "))
random_roll = random.randint(userMinimum, userMaximum)

if userGuess == random_roll:
    print("You guess right! The dice rolled %d" % random_roll)
else:
    print("You guessed wrong! The dice rolled %d" % random_roll)
