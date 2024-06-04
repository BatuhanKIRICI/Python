from list import MENU, resources
import math

turn_on = True

penny = 0.01
nickel = 0.05
dime = 0.10
quarter = 0.25

espresso_price = 1.5
latte_price = 2.5
cappucino_price = 2.5

money = 0

choice_of_customer = input("What would you like? (espresso/latte/cappuccino): ").lower()


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

    diff = round(
        penny * penny_quantity
        + nickel * nickel_quantity
        + dime * dime_quantity
        + quarter * quarter_quantity
        - espresso_price,
        2,
    )

    print(f"${diff}")

elif choice_of_customer == "latte":
    print("Please insert coins!")
    penny_quantity = int(input("How many pennies? "))
    nickel_quantity = int(input("How many nickels? "))
    dime_quantity = int(input("How many dimes? "))
    quarter_quantity = int(input("How many quarters? "))

    diff = round(
        penny * penny_quantity
        + nickel * nickel_quantity
        + dime * dime_quantity
        + quarter * quarter_quantity
        - latte_price,
        2,
    )

    print(f"${diff}")

elif choice_of_customer == "cappucino":
    print("Please insert coins!")
    penny_quantity = int(input("How many pennies? "))
    nickel_quantity = int(input("How many nickels? "))
    dime_quantity = int(input("How many dimes? "))
    quarter_quantity = int(input("How many quarters? "))

    diff = round(
        penny * penny_quantity
        + nickel * nickel_quantity
        + dime * dime_quantity
        + quarter * quarter_quantity
        - cappucino_price,
        2,
    )

    print(f"${diff}")

# print(choice_of_customer)
