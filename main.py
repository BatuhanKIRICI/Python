# def my_function():
#     for i in range(1, 20):
#         if i == 20:
#             print("You got it!")


# my_function()

# pages = 0

# words_per_page = 0

# pages = int(input("Enter number of pages: "))

# words_per_page == int(input("Enter number of words: "))

# total_words = pages * words_per_page

# print(total_words)


def mutate_list(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    print(b_list)


mutate_list([1, 23, 45])
