import random
from Data import instagram_data
from Art import art

print(art)
def generate_random():
    return random.choice(instagram_data)


againest = generate_random()


score = 0
game_over = False

while not game_over:
    compare = againest
    againest = generate_random()

    print(f"Compare A : {compare["name"]} and His profession is : {compare["profession"]} ")
    print(f"Againest B : {againest["name"]} and His profession is : {againest["profession"]} ")
    guess = input("Is B has Highest Followers than A (Y or N) : ").lower()

    if guess == 'y':
        if compare["followers"] < againest["followers"]:
            score += 1
            print(f"Your score = {score}")
        else:
            print("You lost !")
            print(f" A Followers are : {compare["followers"]} and B Followers are :{againest["followers"]} ")
            print(f"Your Final score = {score}")
            game_over = True
            
    elif guess == 'n':
        if compare["followers"] > againest["followers"]:
            score += 1
            print(f"Your  score = {score}")
        else:
            print("You lost !")
            print(f" A Followers are : {compare["followers"]} and B Followers are :{againest["followers"]} ")
            print(f"Your Final score = {score}")
            game_over = True