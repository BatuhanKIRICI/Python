from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)

timmy.shape("turtle")
timmy.color("blue")

my_screen = Screen()

timmy.forward(150)

print(my_screen.canvheight)


my_screen.exitonclick()
