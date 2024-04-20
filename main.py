def prime_number(n):
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
    if is_prime == True:
        print("This is a prime number.")
    else:
        print("This is not a prime number.")


number = int(input("Enter a number: "))

prime_number(n=number)
