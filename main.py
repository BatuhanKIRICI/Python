my_list = []

my_list.append(5)
my_list.append(25)
my_list.append(60)
my_list.append(60)
my_list.append("60")

# print(my_list)
# print(my_list.index("60"))

my_list.insert(1, 133)

# print(my_list)
# print(my_list.count(60))

# print(my_list.index("60"))

my_list.reverse()

# print(my_list)

my_list.remove("60")

my_list.sort()
# my_list.reverse()

print(my_list)

new_item = my_list.pop()

print(my_list, new_item)
