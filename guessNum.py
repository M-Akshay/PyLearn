import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0 
    while guess!=random_number:
        guess = int(input(f"Guess a num from 1 to {x}:"))
        if guess<random_number:
            print("Higher")
        elif guess>random_number:
            print("lower")
    
    print(f"You guessed correct: {random_number}")

def computer_g(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low
        guess = random.randint(low,high)
        feedback = input(f"Is {guess} too high H, too Low L or C:").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    
    print(f"Yay it guessed {guess}")

guess(12)
computer_g(12)
