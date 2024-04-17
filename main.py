import turtle

wn = turtle.Screen()

elan = turtle.Turtle()

distance = 10
elan.speed(5)

for _ in range(30):
    elan.forward(distance)
    elan.left(90)
    distance += 10

wn.exitonclick()
