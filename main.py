week_temps_f = "75.1,77.7,83.2,82.5,81.0,79.5,85.7"

temps_list = week_temps_f.split(",")

sum = 0

for x in temps_list:
    sum += float(x)

avg_temp = sum / (len(temps_list))

print(avg_temp)
