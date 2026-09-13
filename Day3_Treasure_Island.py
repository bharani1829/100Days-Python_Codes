print("Welcome to treasure Island Game ")
direction = input("in which you want to go Left or right : ")

if direction == 'left':
    print("Opps! you fall into deephole\nGameOver ")
elif direction == 'right':
    user_decision = input("do you want to wait or swim : ")
    if user_decision == 'swim':
        print("You are attacked by crocodile..!")
        print("Game over ")
    elif user_decision == 'wait':
        door = input("which door do you want to open(red or yellow or blue) : ")
        if door == 'red':
            print(" It is full of fire")
            print("Game over ")
        elif door == 'yellow':
            print("It is full of lions ")
            print("Game over ")
        elif door == 'blue':
            print("Congratulations you Found Treasure ")
        else:
            print("Invalid door")
    else:
        print("Invalid choice")
else:
    print("Invalid Direction")