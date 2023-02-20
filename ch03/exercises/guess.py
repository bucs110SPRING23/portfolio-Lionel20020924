import random

# generate a random number between 1 and 10 (inclusive)
number = random.randint(1, 10)

# give the user 3 chances to guess the number
for i in range(3):
    guess = int(input("Guess the number between 1 and 10: "))
    
    if guess == number:
        print("Correct!")
        break
    elif guess < number:
        print("Too low")
    else:
        print("Too high")
        
    if i == 2:
        print(f"Sorry, the number was {number}. Better luck next time!")
