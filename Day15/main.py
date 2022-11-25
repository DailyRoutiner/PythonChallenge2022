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
income = 0.0


# print Reports
def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml ")
    print(f"Coffee: {resources['coffee']}g ")
    print(f"Money: ${income} ")


# Check resources sufficient?
def checkResources(ingredient):
    for item in ingredient:
        if ingredient[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


#  Process coins.
def insertCoins():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


# Check transaction successful?
def isTransactionSuccessful(coin, drinkPrice):
    if coin > drinkPrice:
        change = coin - drinkPrice
        print(f"Here is ${round(change,2)} in change")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


# Make Coffee.
def makeCoffee(coffee, selected):
    for item in coffee:
        resources[item] = resources[item] - coffee[item]
    print(f"Here is your {selected} ☕️. Enjoy!")
    cost = MENU[selected]['cost']
    return cost


condition = True

#  What would you like? (espresso/latte/cappuccino):
while condition:
    selected = input("What would you like? (espresso/latte/cappuccino): ").lower()
    # Turn off the Coffee Machine by entering “off” to the prompt.
    if selected == "off":
        condition = False
    elif selected == "report":
        report()
        condition = True
    else:
        coffee = MENU[selected]
        if checkResources(coffee['ingredients']):
            payment = insertCoins()
            if isTransactionSuccessful(payment, coffee['cost']):
                income += makeCoffee(coffee['ingredients'], selected)  # 이건 잘 모르겠다..
                condition = True
