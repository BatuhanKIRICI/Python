import turtle
import math

wn = turtle.Screen()

bob = turtle.Turtle()

bob.right(90)
bob.forward(50)
bob.left(90)
bob.forward(50)
bob.left(90)
bob.forward(50)
bob.left(90)
bob.forward(50)
bob.right(135)

distance = math.sqrt(50 * 50 / 2)

bob.forward(distance)
bob.right(90)
bob.forward(distance)

wn.exitonclick()
