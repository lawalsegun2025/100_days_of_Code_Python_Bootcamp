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

#Write your code below this line 👇
import random

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if player_choice not in range(0, 3):
  print("You Typed an invalid number")
else:
  options = [rock, paper, scissors]

  player_chose = options[player_choice]


  if player_chose == rock:
    print(rock)
  elif player_chose == paper:
    print(paper)
  elif player_chose == scissors:
    print(scissors)

  print("\n")

  # options = [rock, paper, scissors]

  index_num = random.randint(0, len(options) - 1)

  print("Computer chose:\n")
  computer_chose = options[index_num]
  print(computer_chose)

  if player_chose == rock and computer_chose == scissors:
    print("You Win")
  elif player_chose == paper and computer_chose == rock:
    print("You win")
  elif player_chose == scissors and computer_chose == paper:
    print("You win")
  elif player_chose == computer_chose:
    print("It's a draw")
  else:
    print("You lose")