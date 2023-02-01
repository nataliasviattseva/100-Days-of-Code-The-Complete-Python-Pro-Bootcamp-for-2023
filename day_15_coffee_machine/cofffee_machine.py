from data import MENU, resources

total_money = 0


def prepare_coffee():
    """- resourcec + money"""
    water_menu = MENU[answer]["ingredients"]["water"]
    milk_menu = MENU[answer]["ingredients"]["milk"]
    coffee_menu = MENU[answer]["ingredients"]["coffee"]
    resources["water"] -= water_menu


def payment():
    global total_money

    print("Please insert coins.")
    quarters = int(input(" how many quarters?: "))   # 0.25
    dimes = int(input(" how many dimes?: "))         # 0.10
    nickles = int(input(" how many nickles?: "))     # 0.05
    pennies = int(input(" how many pennies?: "))     # 0.01
    paid = quarters * 0.25 + dimes * 0.10 + nickles * 0.1 + pennies * 0.01

    cost = MENU[answer]["cost"]

    if cost > paid:
        print("Sorry that's not enough money. Money refunded.")
    else:
        total_money += paid
        change = paid - cost
        print(f"Here is ${change} in change.")

    print(f"Here is your {answer} ☕️. Enjoy!")


def report():
    """Report how many resources rest"""
    print(f'Water: {resources["water"]} ml')
    print(f'Milk: {resources["milk"]} ml')
    print(f'Coffee: {resources["coffee"]} g')
    print(f"Money: ${total_money}")


continue_work = True

while continue_work:

    answer = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if answer == "report":
        report()
    elif answer == "off":
        continue_work = False
    elif answer in ("espresso", "cappuccino", "latte"):
        prepare_coffee()
        payment()
    else:
        print("Enter a valid value")






