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
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

computer = [rock, paper, scissors]

rand_num = random.randint(0, 2)

comp_selection = computer[rand_num]


player_selection = input("Rock, Paper, or Scissors?\n").lower()

if player_selection == "rock" and comp_selection == paper:
    print(f"{comp_selection}\n{player_selection}\n\nYou lose!")
elif player_selection == "rock" and comp_selection == rock:
    print(f"{comp_selection}\n{player_selection}\n\nDraw!")
elif player_selection == "rock" and comp_selection == scissors:
    print(f"{comp_selection}\n{player_selection}\n\nYou win!")

elif player_selection == "paper" and comp_selection == paper:
    print(f"{comp_selection}\n{player_selection}\n\nDraw!")
elif player_selection == "paper" and comp_selection == rock:
    print(f"{comp_selection}\n{player_selection}\n\nYou win!")
elif player_selection == "paper" and comp_selection == scissors:
    print(f"{comp_selection}\n{player_selection}\n\nYou lose!")

if player_selection == "scissors" and comp_selection == paper:
    print(f"{comp_selection}\n{player_selection}\n\nYou win!")
elif player_selection == "scissors" and comp_selection == rock:
    print(f"{comp_selection}\n{player_selection}\n\nYou lose!")
elif player_selection == "scissors" and comp_selection == scissors:
    print(f"{comp_selection}\n{player_selection}\n\nDraw!")
elif player_selection != ("rock" or "paper" or "scissors"):
    print("You've typed wrong!")
