from random import randint

random_number = randint(1, 10)
user_guess = int(input("Guess a number between 1 and 10: "))

while True:
    if user_guess > random_number:
        user_guess = int(input("Too high, guess again number between 1 and 10: "))
    elif user_guess < random_number:
        user_guess = int(input("Too low, guess again number between 1 and 10: "))
    else:
        print("You guessed it! You won!")
        user = input("Do you want to keep playing? (y/n) ")
        while user not in ['n', 'y', 'N', 'Y']:
            user = input("Wrong input, do you want to keep playing? (y/n) ")
        if user in ['n', 'N']:
            break
        else:
            random_number = randint(1, 10)
            user_guess = int(input("Guess a number between 1 and 10: "))

