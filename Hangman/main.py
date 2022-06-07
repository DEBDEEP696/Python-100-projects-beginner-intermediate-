import random
from hangman_words import word_list
from hangman_art import logo,stages

print(logo)
#Testing code
#word_list = ["ardvark","baboon","camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Create blanks
display = []
for _ in range(word_length):                                       
    display += "_"                                                 

lives = 6                                                                                                                                                                       
end_of_game = False 

while not end_of_game:
    guess = input("Guess a letter : ").lower()
    if guess in display:
        print(f"You've already guessed {guess}")
    for position in range (word_length):                               
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")    ---for debugging---                              
        if letter == guess:                                            
            display[position] = letter
        # else: lives -= 1  ----------- This is wrong beacuse it will go through the chosen word and match it with the guess which will trigger the else condition which is not required---------------    

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the wrod. you lose a life")
        if lives == 0:
            end_of_game = True
            print("YOU LOSE")
            print(f'The solution is {chosen_word} .')             

    #print(display)
    print(f"{' '.join(display)}")

    if "_"  not in display:
        end_of_game = True
        print("YOU WON")
    
    print((stages[lives]))

#------------------------------------------------------------------------------------XX-------------------------------------------------------------------------------------------------

# for l in chosen_word:
#     display += "_"
#---------OR---------
# for i in range(word_length):
#     display.append("_")
#     counter += 1     

# counter = 0
# for l in chosen_word:
#     if letter==guess:
#         display[counter] = l






