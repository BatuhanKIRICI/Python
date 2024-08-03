# with open("newFile.txt", "w") as file:
#     file.write("This is a new file created!")

# with open("newFile.txt", "w") as file:
#     file.writelines(
#         ["This is a new file created.", "\nThis is another line to be added."]
#     )

# with open("newFile.txt", "a") as file:
#     file.writelines(
#         ["This is a new file created.", "\nThis is another line to be added."]
#     )

try:
    with open("sample/newFile.txt", "a") as file:
        file.writelines(
            ["\nThis is a new file created.", "\nThis is another line to be added."]
        )
except FileNotFoundError as e:
    print("ERROR", e)
