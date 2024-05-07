# rainfall_mi = "1.65, 1.46, 2.05, 3.03, 3.35, 3.46, 2.83, 3.23, 3.5, 2.52, 2.8, 1.85"

# num_rainy_months = 0

# rainfall_int = rainfall_mi.split(", ")

# # print(rainfall_int)

# for x in rainfall_int:
#     x = float(x)
#     if x > 3:
#         num_rainy_months += 1

# print(num_rainy_months)


# sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"

# new_list = sentence.split(" ")

# count = 0

# # print(new_list)

# for x in new_list:
#     if x[0] == x[len(x) - 1]:
#         count += 1

# print(count)

# items = [
#     "whirring",
#     "wow!",
#     "calendar",
#     "wry",
#     "glass",
#     "",
#     "llama",
#     "tumultuous",
#     "owing",
# ]

# acc_num = 0

# for item in items:
#     if "w" in item:
#         acc_num += 1


# print(acc_num)

sentence = "python is a high level general purpose programming language that can be applied to many different classes of problems."

num_a_or_e = 0

new_sentence = sentence.split()

for word in new_sentence:
    if "a" in word or "e" in word:
        num_a_or_e += 1

print(num_a_or_e)
