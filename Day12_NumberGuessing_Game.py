import random
logo = '''
  /$$$$$$                                                 /$$     /$$                       /$$   /$$                         /$$                          
 /$$__  $$                                               | $$    | $$                      | $$$ | $$                        | $$                          
| $$  \__/ /$$   /$$  /$$$$$$   /$$$$$$$ /$$$$$$$       /$$$$$$  | $$$$$$$   /$$$$$$       | $$$$| $$ /$$   /$$ /$$$$$$/$$$$ | $$$$$$$   /$$$$$$   /$$$$$$ 
| $$ /$$$$| $$  | $$ /$$__  $$ /$$_____//$$_____/      |_  $$_/  | $$__  $$ /$$__  $$      | $$ $$ $$| $$  | $$| $$_  $$_  $$| $$__  $$ /$$__  $$ /$$__  $$
| $$|_  $$| $$  | $$| $$$$$$$$|  $$$$$$|  $$$$$$         | $$    | $$  \ $$| $$$$$$$$      | $$  $$$$| $$  | $$| $$ \ $$ \ $$| $$  \ $$| $$$$$$$$| $$  \__/
| $$  \ $$| $$  | $$| $$_____/ \____  $$\____  $$        | $$ /$$| $$  | $$| $$_____/      | $$\  $$$| $$  | $$| $$ | $$ | $$| $$  | $$| $$_____/| $$      
|  $$$$$$/|  $$$$$$/|  $$$$$$$ /$$$$$$$//$$$$$$$/        |  $$$$/| $$  | $$|  $$$$$$$      | $$ \  $$|  $$$$$$/| $$ | $$ | $$| $$$$$$$/|  $$$$$$$| $$      
 \______/  \______/  \_______/|_______/|_______/          \___/  |__/  |__/ \_______/      |__/  \__/ \______/ |__/ |__/ |__/|_______/  \_______/|__/      
                                                                                                                                                           
                                                                                                                                                           
                                                                                                                                                           
                                                                                                                                                           '''
print(logo)

choosen_number = random.randint(1,101)

choose_level = input("Choose the level (easy or hard): ").lower()

def level(chances):
    chances = chances
    while chances != 0:
        guess = int(input("Guess the number between 1 to 100 : "))
        if guess == choosen_number:
            print(f"You won ! and You've guessed it correctly ")
            break
        elif guess > choosen_number:
            print("Too high ")
            chances -= 1
        elif guess < choosen_number:
            print("Too low ")
            chances -= 1
        print(f"You've {chances} chances left ")
    if chances == 0:
        print("You lost You didn't guessed it !")
        

if choose_level == 'easy':
    level(10)
elif choose_level == 'hard':
    level(5)
    
      
    


