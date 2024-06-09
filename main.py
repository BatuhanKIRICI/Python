# from turtle import Turtle, Screen

# timmy = Turtle()
# print(timmy)

# timmy.shape("turtle")
# timmy.color("blue")

# my_screen = Screen()

# timmy.forward(150)

# print(my_screen.canvheight)


# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])

print(table)

table.add_column("Type", ["Electric", "Water", "Fire"])

print(table)
