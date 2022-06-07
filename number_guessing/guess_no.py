import random
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def set_difficulty():
    choice = input("Choose a difficulty.Type 'easy' or 'hard' : ")
    if choice == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def random_number():
    return random.randint(1,100)

def checking(guess,num,attempts):
    '''takes guess , original number and no. of attempts, checks them and returns remaining attempts'''
    if guess < num:
        print("Too low")
        return attempts-1
    elif guess > num:
        print("Too high")
        return attempts-1
    else:
        print(f"You got it! The ans is {num}.")
    
def game():
    print("Welcome to the Number guessing game!")
    print("I'm thinking of a number between 1 and 100.")
    num = random_number()
    # print(num)
    turns = set_difficulty()
    guess = 0

    while guess!= num:

        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = checking(guess, num, turns)
        if turns == 0:
            print("You run out of guesses.")
            return
        elif guess!=num:
            print("Guess again.")

from art import logo
print (logo)          
game()