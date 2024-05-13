# scores = "67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74 83 88 80 86 85 70 90 100"
# new_list = scores.split()

# # print(new_list)

# a_scores = 0

# for score in new_list:
#     if int(score) >= 90:
#         a_scores += 1

# # print(a_scores)

# stopwords = ["to", "a", "for", "by", "an", "am", "the", "so", "it", "and", "The"]
# org = "The organization for health, safety, and education"
# acro = ""
# lst = org.split()

# for i in lst:
#     if i in stopwords:
#         lst.remove(i)

# for j in lst:
#     acro += j[0]

# acro = acro.upper()

# stopwords = ["to", "a", "for", "by", "an", "am", "the", "so", "it", "and", "The"]
# sent = "The water earth and air are vital"
# acro = ""
# lst = sent.split()

# for i in lst:
#     if i in stopwords:
#         lst.remove(i)

# for j in lst:
#     acro = acro + j[0] + j[1]
#     if j != lst[-1]:
#         acro += ". "

# acro = acro.upper()

# p_phrase = "was it a car or a cat I saw"
# r_phrase = p_phrase[::-1]

# print(r_phrase)

inventory = [
    "shoes, 12, 29.99",
    "shirts, 20, 9.99",
    "sweatpants, 25, 15.00",
    "scarves, 13, 7.75",
]
for temp in inventory:
    temp = temp.split(",")
    str1 = "The store has{} {}, each for{} USD."
    str1 = str1.format(temp[1], temp[0], temp[2])
    print(str1)
