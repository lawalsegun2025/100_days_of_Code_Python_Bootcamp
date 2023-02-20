from art import logo, vs
from game_data import data
import random
from replit import clear


def format_data(account):
    """Takes the account data and returns the printabel format."""
    # Format the account data into a printabel format
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"


def check_answer(guess, a_followers, b_followers):
    """Takes the user guess and follower counts and return if they got it right"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


#Display art
print(logo)
score = 0

# make the game repeatable.
game_should_continue = True
account_b = random.choice(data)
while game_should_continue:
    # Generate a random account from the data

    # Making account at position B become the next account at position A.
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    # Ask the user for a guess.
    guess = input("Who has more followers? Type 'A' of 'B': ").lower()

    # Check if guess is right or wrong
    ## Get follower count of each accout
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    clear()
    print(logo)

    # Give user feed back
    if is_correct:
        # keeping score.
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}")

    # Clear the screen
