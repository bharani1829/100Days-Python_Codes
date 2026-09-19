logo = '''
  _______ _             _____ _ _            _                        _   _             
 |__   __| |           / ____(_) |          | |       /\             | | (_)            
    | |  | |__   ___  | (___  _| | ___ _ __ | |_     /  \  _   _  ___| |_ _  ___  _ __  
    | |  | '_ \ / _ \  \___ \| | |/ _ \ '_ \| __|   / /\ \| | | |/ __| __| |/ _ \| '_ \ 
    | |  | | | |  __/  ____) | | |  __/ | | | |_   / ____ \ |_| | (__| |_| | (_) | | | |
    |_|  |_| |_|\___| |_____/|_|_|\___|_| |_|\__| /_/    \_\__,_|\___|\__|_|\___/|_| |_|                                                                                        
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
print("Welcome to the Secret Bidding !")

bidding = {}

more_people = True

winner_amount = 0
winner = ""

while more_people:
    key = input("What is your name : ")
    value = int(input("Enter You amount For bid :$"))
    bidding[key] = value
    
    ask_user = input("Is there any one else : (yes or no) :  ").lower()
    
    if ask_user == 'yes':
        print("\n" * 100 )
    elif ask_user == 'no':
        more_people = False
    
    for winners in bidding:
        if bidding[winners] > winner_amount:
            winner = winners
            winner_amount = bidding[winners]
            
    
        

    
print(f'The Winner is {winner} with  ${winner_amount}')
print("Welcome to the Secret Bidding !")

bidding = {}
winner_amount = 0
winner = ""

more_people = True

def select_winner(bidding):
    func_winner_amount = 0
    func_winner = ""
    for winners in bidding:
        if bidding[winners] > func_winner_amount:
            func_winner = winners
            func_winner_amount = bidding[winners]
    return func_winner,func_winner_amount;

while more_people:
    key = input("What is your name : ")
    value = int(input("Enter You amount For bid :$"))
    bidding[key] = value
    
    ask_user = input("Is there any one else : (yes or no) :  ").lower()
    if ask_user == 'yes':
        print("\n" * 100 )
    elif ask_user == 'no':
        more_people = False
    
    winner,winner_amount = select_winner(bidding)
    
            
print(f'The Winner is {winner} with ${winner_amount} Bid')

