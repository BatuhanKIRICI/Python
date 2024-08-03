def divide_by(a, b):
    return a / b


# try:
#     divide_by(40, 1)
# except:
#     print("Something went wrong!")

# try:
#     divide_by(40, 0)
# except Exception as e:
#     print("Something went wrong!", e)
#     print(e.__class__)

try:
    divide_by(40, 0)
except ZeroDivisionError as e:
    print("We can't divide by zero!", e)
except Exception as e:
    print("Something went wrong!", e)
