from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
print("Welcome to the secret auction program. \n")


auction_dict = {}

def add_to_auction(new_user, users_bid):
  auction_dict[new_user] = users_bid
  

other_bidder = True
while other_bidder == True:
  name = input("What is your name?: ")
  bid = int(input("What is your bid?: $"))
  add_to_auction(new_user = name, users_bid = bid)

  next_bidder = input("Are there any other bidders? Type 'yes' or 'no'. \n")
  if next_bidder == "yes":
    clear()
  elif next_bidder == "no":
    
    other_bidder = False
    clear()

highest_bidder = 0
winners_name = ""
#winners_bid = highest_bidder
for user in auction_dict:
  if auction_dict[user] > highest_bidder:
    highest_bidder = auction_dict[user]
    winners_name = user

print(f"The Winner is {winners_name} with a bid of ${highest_bidder}")
    
#print(auction_dict)
    
    
  
  
  