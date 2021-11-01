import random

""" amount_of_dice = rawinput("How many sides on the dice: ") """
userMinimum = int(input("Enter a minimum amount: "))
userMaximum = int(input("Enter a maximum amount: "))

for amount in range(10):
    random_roll = random.randint(userMinimum, userMaximum)
    print(random_roll)
    