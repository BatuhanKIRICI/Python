height =  int(input("Enter your height in cm:\n"))

if height < 120:
    print(f"YOu are not allowed to enter.")
else:
    age =  int(input("Enter your age:\n"))
    if age >= 18:
        print(f"You need to pay 12$")
    else:
        print(f"You need to pay 7$")
