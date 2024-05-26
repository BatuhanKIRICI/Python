import random


def game_play():
    game_is_on = True
    computer_number = random.randrange(1, 100)

    difficulty = input(
        "Select difficulty! Type 'e' for easy, type 'h' for hard. "
    ).lower()

    count = 10

    list_higher = [100]
    list_lower = [0]

    while game_is_on:
        guessed_num = int(input("Guess a number: "))

        if difficulty == "h":
            if guessed_num > computer_number and count > 6:

                list_higher.append(guessed_num)
                count -= 1

                result = f"Too high! Number between {max(list_lower)} and {min(list_higher)}. And you have {count-5} shot to try!"

                print(f"{result}")

            elif guessed_num < computer_number and count > 6:

                list_lower.append(guessed_num)
                count -= 1

                result = f"Too low! Number between {max(list_lower)} and {min(list_higher)}. And you have {count-5} shot to try!"

                if (count - 5) > 0:
                    print(f"{result}")

            elif guessed_num == computer_number and count > 6:

                result = f"Congratulations!!!"

                print(f"{result}")
                play_again = (
                    input("Do you want to play again? (yes/no): ").strip().lower()
                )
                if play_again == "y":
                    difficulty = input(
                        "Select difficulty! Type 'e' for easy, type 'h' for hard. "
                    ).lower()
                    computer_number = random.randrange(1, 100)
                    count = 10

                    list_higher = [100]
                    list_lower = [0]
                    continue
                else:
                    print("Goodbye!")
                    break

            else:
                result = f"You've got no shot! You've lost the game! The number was {computer_number}."
                print(f"{result}")
                play_again = (
                    input("Do you want to play again? (yes/no): ").strip().lower()
                )
                if play_again == "y":
                    difficulty = input(
                        "Select difficulty! Type 'e' for easy, type 'h' for hard. "
                    ).lower()
                    computer_number = random.randrange(1, 100)
                    count = 10

                    list_higher = [100]
                    list_lower = [0]
                    continue
                else:
                    print("Goodbye!")
                    break

        elif difficulty == "e":
            if guessed_num > computer_number and count > 1:

                list_higher.append(guessed_num)
                count -= 1
                result = f"Too high! Number between {max(list_lower)} and {min(list_higher)}. And you have {count} shot to try!"
                print(f"{result}")

            elif guessed_num < computer_number and count > 1:

                list_lower.append(guessed_num)
                count -= 1
                result = f"Too low! Number between {max(list_lower)} and {min(list_higher)}. And you have {count} shot to try!"
                if (count) > 0:
                    print(f"{result}")

            elif guessed_num == computer_number and count > 1:
                result = f"Congratulations!!!"
                print(f"{result}")
                play_again = (
                    input("Do you want to play again? (yes/no): ").strip().lower()
                )
                if play_again == "y":
                    difficulty = input(
                        "Select difficulty! Type 'e' for easy, type 'h' for hard. "
                    ).lower()
                    computer_number = random.randrange(1, 100)
                    count = 10

                    list_higher = [100]
                    list_lower = [0]
                    continue
                else:
                    print("Goodbye!")
                    break

            else:
                result = f"You've got no shot! You've lost the game! The number was {computer_number}."
                print(f"{result}")
                play_again = (
                    input("Do you want to play again? (yes/no): ").strip().lower()
                )
                if play_again == "y":
                    difficulty = input(
                        "Select difficulty! Type 'e' for easy, type 'h' for hard. "
                    ).lower()
                    computer_number = random.randrange(1, 100)
                    count = 10

                    list_higher = [100]
                    list_lower = [0]
                    continue
                else:
                    print("Goodbye!")
                    break


game_play()
