'''def my_function():
    global my_variable
    my_variable = 8
    print(my_variable)


my_variable = 4
print(my_variable)
my_function()
print(my_variable)'''


def fizzbuzz(start_number, end_number, first_divisor, second_divisor):
    for i in range(start_number, end_number+1):
        if i % first_divisor == 0 and i % second_divisor == 0:
            print("Fizzbuzz")
        elif i % first_divisor == 0:
            print("Fizz")
        elif i % second_divisor == 0:
            print("Buzz")
        else:
            print(i)
fizzbuzz(30,40,8,9)