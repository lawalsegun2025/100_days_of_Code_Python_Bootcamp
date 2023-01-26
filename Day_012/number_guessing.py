#Number Guessing Game Objectives:

# Include an ASCII art logo.
## Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from art import logo
import random
print(logo)


print("Welcom to the Number Guessing Game!")
print("I am thinking of a number between 1 to 10.")
#Computer randomly Chooses a number from 1 to 100 and saves it as actual_answer
actual_answer = random.randint(1, 100)
#print(f"Actual answer = {actual_answer}")

# Ask the user to choose and input a difficulty type
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
chances = 0


if difficulty == "easy":
  chances = 10
  print(f"You have {chances} attempts remaining to guess the number.")
else:
  chances = 5
  print(f"You have {chances} attempts remaining to guess the number.")


end_game = False
while not end_game:
  if chances == 0:
    print("You have run out of attempts!")
    print("GAME OVER!!!")
    end_game = True
  else:
    
    user_answer = int(input("Make an guess: "))
    if user_answer == actual_answer:
      print(f"You got it! the answer was {actual_answer}")
      end_game = True
    elif user_answer < actual_answer:
      print("Too low.")
      chances -= 1
      print("Guess again")
      print(f"You have {chances} attempts remaining to guess the number.")
    elif user_answer > actual_answer:
      print("Too high")
      chances -= 1
      print("Guess again")
      print(f"You have {chances} attempts remaining to guess the number.")
    
  
  

