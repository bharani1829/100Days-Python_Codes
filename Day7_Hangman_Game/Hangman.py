import random 
from Hangman_related import words_list,logo
from Hangman_related import hang_toy

choosen_word = random.choice(words_list)

print(logo)

placeholder = ""

for position in choosen_word:
    placeholder += '_'

lives = 6



corrected = []
game_over = False

while not game_over:
    print(f"====================={lives} lives left=========================")
    
    display = ""
    guess = input("Guess a letter : ").lower()
    if guess in corrected:
        print("You've Already Guessed It")
    
    for word in choosen_word:
        if word == guess:
            display += word
            corrected.append(word)
        elif word in corrected:
            display += word
        else:
            display += '_'

    
    if guess not in choosen_word:
        lives -= 1
        if lives == 0:
            print(f"================================You lost ! Word Is {choosen_word}")
            game_over = True
    
    if '_' not in display:
        game_over = True
        print(f"You won you've guessed it Correct : {choosen_word}")
    
    print(display)  
     
    print(hang_toy[lives])  
