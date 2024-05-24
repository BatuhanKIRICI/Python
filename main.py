import random

computer_number = random.randrange(1, 100)

difficulty = input("Select difficulty! Type 'e' for easy, type 'h' for hard. ").lower()

count = 10

list_higher = [100]
list_lower = [0]

game_is_on = True


while game_is_on:

    guessed_num = int(input("Guess a number: "))

    if difficulty == "h":
        if guessed_num > computer_number and count > 6:

            list_higher.append(guessed_num)
            count -= 1
            print(
                f"Too high! Number between {max(list_lower)} and {min(list_higher)}. And you have {count-5} shot to try!"
            )

        elif guessed_num < computer_number and count > 6:

            list_lower.append(guessed_num)
            count -= 1
            if (count - 5) > 0:
                print(
                    f"Too low! Number between {max(list_lower)} and {min(list_higher)}. And you have {count-5} shot to try!"
                )
            else:
                print(f"You've got no shot!")

        elif guessed_num == computer_number and count > 6:
            print(f"Congratulations!!!")
            break
        else:
            print(f"You've lost the game!")
            break

    elif difficulty == "e":
        if guessed_num > computer_number and count > 1:

            list_higher.append(guessed_num)
            count -= 1
            print(
                f"Too high! Number between {max(list_lower)} and {min(list_higher)}. And you have {count} shot to try!"
            )

        elif guessed_num < computer_number and count > 1:

            list_lower.append(guessed_num)
            count -= 1
            if (count) > 0:
                print(
                    f"Too low! Number between {max(list_lower)} and {min(list_higher)}. And you have {count} shot to try!"
                )
            else:
                print(f"You've got no shot!")

        elif guessed_num == computer_number and count > 1:
            print(f"Congratulations!!!")
            break
        else:
            print(f"You've lost the game!")
            break
