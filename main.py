# original_str = "The quick brown rhino jumped over the extremely lazy fox"

# num_list = original_str.split(" ")

# # print(num_words_list)

# num_words_list = []

# for i in num_list:
#     num_list = num_words_list.append(len(i))

# print(num_words_list)

import turtle

wn = turtle.Screen()
alex = turtle.Turtle()

for i in range(100):
    alex.speed(i + 1)
    alex.forward(10)
    alex.left(i + 10)

wn.exitonclick()
