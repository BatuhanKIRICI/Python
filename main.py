import turtle

screen = turtle.Screen()
screen.bgcolor("lightgreen")
alex = turtle.Turtle()
alex.color("red")
alex.pensize(3)

tina = turtle.Turtle()
tina.color("blue")
tina.pensize(5)

alex.forward(150)
alex.left(90)
alex.forward(200)

tina.right(135)
tina.forward(50)
tina.right(75)
tina.forward(80)

screen.exitonclick()
