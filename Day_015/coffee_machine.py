MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}



def current_resources():
    """Checks the quantity of current resources remaining to prepare coffee and returns a proper format"""
    water_level = resources["water"]
    milk_level = resources["milk"]
    coffee_level = resources["coffee"]
    return f"Water: {water_level}ml\nMilk: {milk_level}ml\nCoffee: {coffee_level}g\nMoney: ${money}"


def resources_sufficient(request, MENU, resources):
    """Takes drink name and check if there is enough resources to make that drink"""
    global continue_making_drink
    if request == "espresso":
        if resources["water"] < MENU[request]["ingredients"]["water"]:
            continue_making_drink = False
            return f"Sorry there is not enough water."
        elif resources["coffee"] < MENU[request]["ingredients"]["coffee"]:
            continue_making_drink = False
            return f"Sorry there is ot enough coffee"
    elif request == "latte":
        if resources["water"] < MENU[request]["ingredients"]["water"]:
            continue_making_drink = False
            return f"Sorry there is not enough water."
        elif resources["milk"] < MENU[request]["ingredients"]["milk"]:
            continue_making_drink = False
            return f"Sorry there is not enough milk."
        elif resources["coffee"] < MENU[request]["ingredients"]["coffee"]:
            continue_making_drink = False
            return f"Sorry there is ot enough coffee"
    elif request == "cappuccino":
        if resources["water"] < MENU[request]["ingredients"]["water"]:
            continue_making_drink = False
            return f"Sorry there is not enough water."
        elif resources["milk"] < MENU[request]["ingredients"]["milk"]:
            continue_making_drink = False
            return f"Sorry there is not enough milk."
        elif resources["coffee"] < MENU[request]["ingredients"]["coffee"]:
            continue_making_drink = False
            return f"Sorry there is ot enough coffee"


def check_transaction_success(request, MENU, coins_value):
    """Takes in drink name and the value of the coins inserted and checks if it is enough to pay for the drink"""
    global transaction_successful
    global money
    if request in ["espresso", "latte", "cappuccino"]:
        # TODO: 6a. The user inserted less money
        if coins_value < MENU[request]['cost']:
            transaction_successful = False
            return "Sorry that's not enough money. Money refunded."
        # TODO: 6b. The user inserted enough money
        elif coins_value == MENU[request]['cost']:
            money += MENU[request]['cost']
        # TODO: 6c. The user inserted too much money
        elif coins_value > MENU[request]['cost']:
            money += MENU[request]['cost']
            balance = round((coins_value - MENU[request]['cost']), 2)
            return f"Here is ${balance} dollars in change"


def deduct_from_resources(request, MENU, resources):
    #global resources
    if request == "espresso":
        resources["water"] -= MENU[request]["ingredients"]["water"]
        resources["coffee"] -= MENU[request]["ingredients"]["coffee"]
        return f"Here is your {request}. Enjoy!"
    else:
        resources["water"] -= MENU[request]["ingredients"]["water"]
        resources["milk"] -= MENU[request]["ingredients"]["milk"]
        resources["coffee"] -= MENU[request]["ingredients"]["coffee"]
        return f"Here is your {request}. Enjoy!"




money = 0

# TODO: 1b. The prompt should show every time the an action is completed
turn_off = False
while not turn_off:
    continue_making_drink = True
    transaction_successful = True
    quarters = 0.25
    dimes = 0.10
    nickles = 0.05
    pennies = 0.01

    # TODO: 1. Prompt the user to input a request
    request = input(
        " What would you like? (espresso/latte/cappuccino): ").lower()

    # TODO: 1a Check user input to decide what action to take
    # TODO: 2. turn off coffee machine if request == "off"
    if request == "off":
        turn_off = True
        break
    elif request == "report":
        # TODO: 3a Print report
        print(current_resources())
        continue
    elif request in ["espresso", "latte", "cappuccino"]:
        # TODO: 4a Check if resources is sufficient to make drink else it should not continue making drink
        print(resources_sufficient(request, MENU, resources))
    if continue_making_drink == False:
        continue
    else:
        pass
    # TODO: 5 Process coins
    # TODO 5a: If there are sufficient resources to make the drink selected, then prompt the user to insert coin
    print("Please insert coins.")

    # TODO: 5 Process coins inserted
    quart_value = quarters * int(input("how many quarters?: "))
    dime_value = dimes * int(input("how many dimes?: "))
    nickel_value = nickles * int(input("how many nickles?: "))
    penny_value = pennies * int(input("how many pennies?: "))

    coins_value = quart_value + dime_value + nickel_value + penny_value

    # TODO: 6 Check transaction successful:
    print(check_transaction_success(request, MENU, coins_value))
    if transaction_successful == False:
        continue

    # TODO: 7. Make coffee
    # TODO: 7a. if transaction is successful and there are enough resources, deduct ingredient to make the drink from resources.
    print(deduct_from_resources(request, MENU, resources))

money = 0

# TODO: 1b. The prompt should show every time the an action is completed
turn_off = False
while not turn_off:
	continue_making_drink = True
	transaction_successful = True
	quarters = 0.25
	dimes = 0.10
	nickles = 0.05
	pennies = 0.01

	# TODO: 1. Prompt the user to input a request
	request = input(
	    " What would you like? (espresso/latte/cappuccino): ").lower()

	# TODO: 1a Check user input to decide what action to take
	# TODO: 2. turn off coffee machine if request == "off"
	if request == "off":
		turn_off = True
		break
	elif request == "report":
		# TODO: 3a Print report
		print(current_resources())
		continue
	elif request in ["espresso", "latte", "cappuccino"]:
		# TODO: 4a Check if resources is sufficient to make drink else it should not continue making drink
		print(resources_sufficient(request, MENU, resources))
	if continue_making_drink == False:
		continue
	# TODO: 5 Process coins
	# TODO 5a: If there are sufficient resources to make the drink selected, then prompt the user to insert coin
	print("Please insert coins.")

	# TODO: 5 Process coins inserted
	quart_value = quarters * int(input("how many quarters?: "))
	dime_value = dimes * int(input("how many dimes?: "))
	nickel_value = nickles * int(input("how many nickles?: "))
	penny_value = pennies * int(input("how many pennies?: "))

	coins_value = quart_value + dime_value + nickel_value + penny_value

	# TODO: 6 Check transaction successful:
	print(check_transaction_success(request, MENU, coins_value))
	if transaction_successful == False:
		continue
