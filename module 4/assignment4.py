import random

secret_number = random.randint(1, 10)

while True:
    guess = int(input("Guess a number (1-10): "))

    if guess > secret_number:
        print("Guess a number (1-10): Too high")
    elif guess < secret_number:
        print("Guess a number (1-10): Too low")
    else:
        print("Guess a number (1-10): Correct")
        break