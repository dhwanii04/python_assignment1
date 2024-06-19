def sum_of_digits(number):
    sum_digits = 0
    while number >0:
        digit= number % 10
        sum_digits += digit
        number//= 10
        return sum_digits

num = int(input("enter a number "))
result = sum_of_digits(num)
print("the sum of digits is :", result)

