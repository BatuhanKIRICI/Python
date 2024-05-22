enemies = 3


def increase_enemies():
    global enemies
    enemies += 1
    print(f"Number of enemies is {enemies}.")


increase_enemies()
print(f"Number of enemies is {enemies}.")
