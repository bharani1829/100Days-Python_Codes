import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

user_choice = int(input("Enter your choice: 0 for Rock, 1 for Paper, or 2 for Scissor: "))

computer_choice = random.randint(0, 2)
images = [rock, paper, scissor]

if user_choice >= 0 and user_choice < 3:
    print(f"You chose:\n{images[user_choice]}")
    print(f"Computer chose:\n{images[computer_choice]}")

if user_choice >= 3 or user_choice < 0:
    print("Invalid choice! You lose.")
elif (
    (user_choice == 0 and computer_choice == 2)
    or (user_choice == 1 and computer_choice == 0)  #here ()--> used for  multiline condition for clean code
    or (user_choice == 2 and computer_choice == 1)
):
    print("You won!")
elif user_choice == computer_choice:
    print("It's a tie!")
else:
    print("You lose!")
