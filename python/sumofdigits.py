def sum_of_digit(n):
    if n< 10:
        return n
    else:
        return n%10 + sum_of_digit(n/10)

number = int(input("Enter number: "))
digit_sum = sum_of_digit(number)
print("Sum of digit of number %d is %d." % (number,digit_sum))
