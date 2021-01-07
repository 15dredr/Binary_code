'''def my_function(i):
    num = i + 1
    if i < 100:
        print(num)
        my_function(num)
    else:
        print("Done")


my_function(10)
'''

'''def factorial(number):
    for i in range((number - 1), 1, -1):
        number = number * i
    return number


factorial_number = int(input("What number do you want the factorial to?"))
print(factorial(factorial_number))'''

'''def factorial(n):
    if n == 0:
        sum = 1
    else:
        sum = n * factorial(n - 1)
    return sum


my_answer = factorial(4)
print(my_answer)
'''
'''initial_balance = float(input("Input Initial Balance"))
desired_balance = float(input("Input desired balance"))
interest_percent = float(input("Input annual percentage for interest as a decimal e.g 4% as 0.04 "))


def how_many_years(initial, desired, intrest):
    years = 0
    if initial < desired:
        initial = initial * intrest'''


def interest(current_value, percentage, final, year):
    if current_value > final:
        return 1 + year
    else:
        return interest(current_value * percentage, percentage, final, year + 1)


print(interest(100, 1.02, 110, 0))
