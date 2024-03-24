height = float(input("Enter your height in m:\n"))
weight = int(input("Enter your weight in kg:\n"))

BMI = round((weight / height**2), 2)

if BMI <= 18.29:
    print(f"Your BMI is {BMI}.You are underweight.")
elif BMI > 18.29 and BMI <= 22:
    print(f"Your BMI is {BMI}.You have normalweight.")
elif BMI > 22 and BMI <= 28.51:
    print(f"Your BMI is {BMI}.You are slightly overweight.")
elif BMI > 28.51 and BMI <= 32.56:
    print(f"Your BMI is {BMI}.You are obese.")
else:
    print(f"Your BMI is {BMI}.You are clinically obese.")
