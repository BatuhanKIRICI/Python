import turtle

wn = turtle.Screen()
alex = turtle.Turtle()

for color in ["yellow", "red", "green", "blue"]:
    alex.color(color)
    alex.forward(50)
    alex.left(90)

wn.exitonclick()
