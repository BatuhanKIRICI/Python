height =  int(input("Enter your height in cm:\n"))
limit_age = 12

if height < 120:
    print(f"YOu are not allowed to enter.")
else:
    age =  int(input("Enter your age:\n"))
    if age >= 18:
        print(f"You need to pay 12$")
    elif age >= 12 and age <18:
        print(f"You need to pay 7$")
    else:
        print(f"You are smaller than {limit_age}. You need to pay 5$.")
