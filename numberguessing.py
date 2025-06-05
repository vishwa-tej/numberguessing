import random

def guess(x):
    rand_num = random.randint(1, x)
    user_guess = 0

    print(f"\n Welcome to the Number Guessing Game! (1 to {x})")

    while user_guess != rand_num:
        try:
            user_guess = int(input(f"\nEnter your guess: "))
            if user_guess < rand_num:
                print(" Too low! Try again.")
            elif user_guess > rand_num:
                print(" Too high! Try again.")
        except ValueError:
            print(" Please enter a valid number!")

    print(f"\n Congratulations! You guessed the number: {rand_num}")

# Run the game
guess(10)
