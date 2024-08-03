def sum(*args):
    sum = 0
    for x in args:
        sum += x
    return sum


print(sum(4, 9, 8, 56))


def sum(**kwargs):
    sum = 0
    for k, v in kwargs.items():
        sum += v
    return round(sum, 2)


print(sum(coffee=3.00, tea=2.25, cake=5.99))
