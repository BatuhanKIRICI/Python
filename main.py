programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",
}

print(programming_dictionary["Bug"])

programming_dictionary["New_Bug"] = "System failed!"

print(programming_dictionary["New_Bug"])

# Create a new dictionary
empty_dictionary = {}

# Wiping an existing dictionary
programming_dictionary = {}

print(programming_dictionary)

# Edit an item in dictionary
programming_dictionary["Bug"] = "A moth in your computer."

print(programming_dictionary)
