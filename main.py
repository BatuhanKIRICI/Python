from list import MENU, resources
import math


def coffee_machine():

    turn_on = False

    penny = 0.01
    nickel = 0.05
    dime = 0.10
    quarter = 0.25

    espresso_price = 1.5
    latte_price = 2.5
    cappucino_price = 2.5

    money = 100.00

    machine = input("Turn on the machine? (yes/no): ").lower()

    if machine == "yes":
        turn_on = True
    elif machine == "no":
        turn_on = False

    while turn_on == True:

        choice_of_customer = input(
            """What would you like? (espresso/latte/cappuccino or "off" to turn off the machine") """
        ).lower()

        if choice_of_customer == "report":
            for item in resources:
                quantity = resources[item]
                if item == "water" or item == "milk":
                    print(f"{item.title()}: {quantity}ml")
                else:
                    print(f"{item.title()}: {quantity}g")
                    print(f"Money: ${money}")
        elif choice_of_customer == "espresso":
            print("Please insert coins!")
            penny_quantity = int(input("How many pennies? "))
            nickel_quantity = int(input("How many nickels? "))
            dime_quantity = int(input("How many dimes? "))
            quarter_quantity = int(input("How many quarters? "))

            resources["water"] -= MENU["espresso"]["ingredients"]["water"]
            resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]

            money += MENU["espresso"]["cost"]

            diff = round(
                penny * penny_quantity
                + nickel * nickel_quantity
                + dime * dime_quantity
                + quarter * quarter_quantity
                - espresso_price,
                2,
            )

        elif choice_of_customer == "latte":
            print("Please insert coins!")
            penny_quantity = int(input("How many pennies? "))
            nickel_quantity = int(input("How many nickels? "))
            dime_quantity = int(input("How many dimes? "))
            quarter_quantity = int(input("How many quarters? "))

            resources["water"] -= MENU["latte"]["ingredients"]["water"]
            resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
            resources["milk"] -= MENU["latte"]["ingredients"]["milk"]

            money += MENU["latte"]["cost"]

            diff = round(
                penny * penny_quantity
                + nickel * nickel_quantity
                + dime * dime_quantity
                + quarter * quarter_quantity
                - latte_price,
                2,
            )

        elif choice_of_customer == "cappuccino":
            print("Please insert coins!")
            penny_quantity = int(input("How many pennies? "))
            nickel_quantity = int(input("How many nickels? "))
            dime_quantity = int(input("How many dimes? "))
            quarter_quantity = int(input("How many quarters? "))

            resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
            resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
            resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]

            money += MENU["cappuccino"]["cost"]

            diff = round(
                penny * penny_quantity
                + nickel * nickel_quantity
                + dime * dime_quantity
                + quarter * quarter_quantity
                - cappucino_price,
                2,
            )
        elif choice_of_customer == "off":
            break

        if diff >= 0:
            print(f"Here is ${diff} dollars in change. Preparing coffee...")
        else:
            print("Sorry that's not enough money. Money refunded.")


coffee_machine()
