total = float(input("Total money: "))

percent = int(input("How much percent? "))/100

bill_total = total + total*percent

person = int(input("How many people? "))

bill_per_person = bill_total/person

print(round(bill_per_person,2))