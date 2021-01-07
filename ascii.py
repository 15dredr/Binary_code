my_number = 120
my_ascii_symbol = chr(my_number)
print(my_ascii_symbol)


def symbol_into_hexadecimal(ascii_symbol):
    number = ord(ascii_symbol)
    hex_number = hex(number)
    return hex_number


def degrees_to_angle(current_angle, desired_angle):
    angle_between =