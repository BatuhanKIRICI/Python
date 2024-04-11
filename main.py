fizzbuzz = range(1, 101)

for num in fizzbuzz:
    if num % 3 == 0 and num % 5 != 0:
        num = "fizz"

    elif num % 3 != 0 and num % 5 == 0:
        num = "buzz"

    elif num % 3 == 0 and num % 5 == 0:
        num = "fizzbuzz"
    print(num)
