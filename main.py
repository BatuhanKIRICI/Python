rainfall_mi = "1.65, 1.46, 2.05, 3.03, 3.35, 3.46, 2.83, 3.23, 3.5, 2.52, 2.8, 1.85"

num_rainy_months = 0

rainfall_int = rainfall_mi.split(", ")

# print(rainfall_int)

for x in rainfall_int:
    x = float(x)
    if x > 3:
        num_rainy_months += 1

print(num_rainy_months)
