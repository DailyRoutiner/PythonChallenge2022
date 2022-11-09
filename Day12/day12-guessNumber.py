from art import logo
import random

print(logo)
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100")
answer = random.randint(1, 100)
def setLevel():
    level = input("Choose a difficulty. Type 'easy' and 'hard': ")
    if level == "easy":
        count = 10
    else:
        count = 5
    return count

count = setLevel()
guessNumber = 0
while answer != guessNumber:
    print(f"You have {count} attempts remaining to guess the number.")
    guessNumber = int(input("Make a guess: "))
    
    if answer == guessNumber:
        print(f"You got it ! Answer is {answer}")
    elif answer > guessNumber:
        print("Too low")
        count = count - 1
    else:
        print("Too high")
        count = count - 1
    
    if count == 0:
        print("You've run out of guesses, You lose")
        break
    elif answer != guessNumber:
        print("Guess again")
    
   

    