import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper "
                      "or 2 for Scissors.\n"))
computer_choice = random.randint(0, 2)

print(game_images[player_choice])
print(f"Computer chose:\n{game_images[computer_choice]}")

if player_choice == 0:
    if computer_choice == 0:
        print("It's a tie!")
    elif computer_choice == 1:
        print("You lose!")
    else:
        print("You win!")
elif player_choice == 1:
    if computer_choice == 0:
        print("You win!")
    elif computer_choice == 1:
        print("It's a tie!")
    else:
        print("You lose!")
elif player_choice == 2:
    if computer_choice == 0:
        print("You lose!")
    elif computer_choice == 1:
        print("You win!")
    else:
        print("It's a tie!")
else:
    print("Invalid option. You lose!")


# First solution
# if player_choice == 0:
#     print(f"{rock}")
#     if computer_choice == 0:
#         print(f"Computer chose:\n{rock}")
#         print("It's a tie!")
#     elif computer_choice == 1:
#         print(f"Computer chose:\n{paper}")
#         print("You lose!")
#     else:
#         print(f"Computer chose:\n{scissors}")
#         print("You win!")
# elif player_choice == 1:
#     print(f"{paper}")
#     if computer_choice == 0:
#         print(f"Computer chose:\n{rock}")
#         print("You win!")
#     elif computer_choice == 1:
#         print(f"Computer chose:\n{paper}")
#         print("It's a tie!")
#     else:
#         print(f"Computer chose:\n{scissors}")
#         print("You lose!")
# elif player_choice == 2:
#     print(f"{scissors}")
#     if computer_choice == 0:
#         print(f"Computer chose:\n{rock}")
#         print("You lose!")
#     elif computer_choice == 1:
#         print(f"Computer chose:\n{paper}")
#         print("You win!")
#     else:
#         print(f"Computer chose:\n{scissors}")
#         print("It's a tie!")
# else:
#     print("Invalid option :(")