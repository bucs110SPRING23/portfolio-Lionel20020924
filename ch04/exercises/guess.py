import random

# generate a random number between 1 and 10 (inclusive)
number = random.randint(1, 1000)
tries = 0

# give the user 1000 chances to guess the number
for i in range(1000):
    guess = int(input("Guess the number between 1 and 1000: "))
    
    if guess == number:
        print("Correct!")
        print(tries)
        break
    elif guess < number:
        print("Too low")
        tries  = tries +1 
    else:
        print("Too high")
        tries = tries + 1 
        
    if i == 1000:
        print(f"Sorry, the number was {number}. Better luck next time!")