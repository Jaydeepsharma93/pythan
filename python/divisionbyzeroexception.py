a = 10
b = int(input("Enter num : "))
try:
    result = a / b
except ZeroDivisionError:
    print("You can't divide by zero!")
    result = None