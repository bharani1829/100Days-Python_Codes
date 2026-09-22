# Black Jack Game
print("====================Welcome to BlackJack21 Game=========================")


import random

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
game_over = False

user_card = []
computer_card = []


for _ in range(2):
    user_card.append(random.choice(cards))
    computer_card.append(random.choice(cards))


def draw_user_card():
    user_card.append(random.choice(cards))


def draw_computer_card():
    computer_card.append(random.choice(cards))


def f_user_score():
    temp_userscore = sum(user_card)
    users_ace = user_card.count(11)
    while temp_userscore > 21 and users_ace != 0:
        if 11 in user_card and temp_userscore > 21:
            temp_userscore -= 10
            users_ace -= 1
    return temp_userscore


def f_computer_score():
    temp_computerscore = sum(computer_card)
    computers_ace = computer_card.count(11)
    while temp_computerscore > 21:
        if 11 in computer_card and computers_ace != 0:
            temp_computerscore -= 10
            computers_ace -= 1
    return temp_computerscore


user_score = f_user_score()
computer_score = f_computer_score()

ask_user = input("do you want to play the game (y or n) : ").lower()


while not game_over:
    if ask_user == "y":
        if f_user_score() == 21:
            print(f"Black jack You won ! and user score is {f_user_score()} ")
        print(
            f"the first two cards of the user : {user_card} and current score is {f_user_score()}"
        )
        print(f"The dealer card is : {computer_card[0]}")
    again = input("do you want to hit or stand : (h or s)").lower()

    if again == "h":
        draw_user_card()
        if f_user_score() > 21:
            print(
                f"user bust and user score is : {f_user_score()} and cards are {user_card}"
            )
            game_over = True
            break
        print(f"the cards of user : {user_card} and current score is {f_user_score()}")
    elif again == "s":
        if f_user_score() == f_computer_score():
            print(
                f"Its a Tie : user score is = {f_user_score()} and dealer score is : {f_computer_score()} "
            )
            
            break
        if f_user_score() > f_computer_score() or f_computer_score() > 21:
            print(
                f"user Win and  user score is : {f_user_score()} and cards are {user_card} "
            )
            print(f"dealer score is : {f_computer_score()} and cards are {computer_card} ")
            game_over = True
            break
        else:
            while f_computer_score() < 17:
                draw_computer_card()
            if f_computer_score() > f_user_score() or f_user_score() > 21:
                print(
                    f"Dealer Win and  dealer score is : {f_computer_score()} and cards are {computer_card} "
                )
                game_over = True
                break
    else:
        print("ok. Bye , namaste ")

