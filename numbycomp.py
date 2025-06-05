import random

def comp_guess(x):
    low = 1
    high = x
    feedback = ''

    print(f"\nThink of a number between 1 and {x} and I'll try to guess it!")

    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        
        feedback = input(f"Is {guess} too low (l), too high (h), or correct (c)? ").lower()

        if feedback == 'l':
            low = guess + 1
        elif feedback == 'h':
            high = guess - 1

    print(f"\n Yay! The computer guessed your number: {guess}")

comp_guess(10)
