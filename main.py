# size = "s"
size = str(input("Size(s,m or l):\n"))

bill = 15

add_pepperoni = input("y or n:\n")

add_cheese = input("y or n:\n")

if size == "s":
    if add_pepperoni == "n" and add_cheese == "n":
        print(bill)
    elif add_pepperoni == "n" and add_cheese == "y":
        print(bill + 1)
    elif add_pepperoni == "y" and add_cheese == "n":
        print(bill + 2)
    elif add_pepperoni == "y" and add_cheese == "y":
        print(bill + 3)

if size == "m":
    bill = 20
    if add_pepperoni == "n" and add_cheese == "n":
        print(bill)
    elif add_pepperoni == "n" and add_cheese == "y":
        print(bill + 1)
    elif add_pepperoni == "y" and add_cheese == "n":
        print(bill + 3)
    elif add_pepperoni == "y" and add_cheese == "y":
        print(bill + 4)

if size == "l":
    bill = 25
    if add_pepperoni == "n" and add_cheese == "n":
        print(bill)
    elif add_pepperoni == "n" and add_cheese == "y":
        print(bill + 1)
    elif add_pepperoni == "y" and add_cheese == "n":
        print(bill + 3)
    elif add_pepperoni == "y" and add_cheese == "y":
        print(bill + 4)
