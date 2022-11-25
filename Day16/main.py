from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu = Menu()
coffee_maker = CoffeeMaker()
coin = MoneyMachine()

is_on = True
while is_on:
    options = menu.get_items()
    # print report
    answer = input(f"What would you like? ({options}): ")
    if answer == "off":
        is_on = False
    elif answer == "report":
        coffee_maker.report()
        coin.report()
    else:
        item = menu.find_drink(answer)
        # Check resources sufficient?
        if coffee_maker.is_resource_sufficient(item):
            # process coin and check transaction successful? cost
            if coin.make_payment(item.cost):
                coffee_maker.make_coffee(item)