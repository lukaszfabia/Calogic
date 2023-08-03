import re
import classes.Calculator.Other as oth


def preprocess(users_input):
    factorial_pattern = r"([+]?\d*)!"  # pattern for factorial
    power_pattern = r"([+]?\d*)\^([+]?\d*)"  # pattern for power
    square_root_pattern = r"sqrt\((\d+(\.\d+)?)\)"  # pattern for square root
    absolute_value_pattern = r"\|(-?\d+(\.\d+)?)\|"  # pattern for absolute value
    cube_root_pattern = r"cbrt\((\d+(\.\d+)?)\)"  # pattern for cube root
    inversion_pattern = r"1/(-?\d+(\.\d+)?)"  # pattern for inversion
    floor_pattern = r"floor\((-?\d+(\.\d+)?)\)"  # pattern for floor
    ceil_pattern = r"ceil\((-?\d+(\.\d+)?)\)"  # pattern for ceil

    if re.search(factorial_pattern, users_input):
        return oth.factorial(int(re.search(factorial_pattern, users_input).group(1)))

    if re.search(power_pattern, users_input):
        return (oth.power(int(re.search(power_pattern, users_input).group(1)),
                          int(re.search(power_pattern, users_input).group(2))))

    if re.search(square_root_pattern, users_input):
        return oth.square_root(int(re.search(square_root_pattern, users_input).group(1)))

    if re.search(absolute_value_pattern, users_input):
        return oth.absolute_value(float(re.search(absolute_value_pattern, users_input).group(1)))

    if re.search(cube_root_pattern, users_input):
        return oth.cube_root(int(re.search(cube_root_pattern, users_input).group(1)))

    if re.search(inversion_pattern, users_input):
        return oth.inversion(float(re.search(inversion_pattern, users_input).group(1)))

    if re.search(floor_pattern, users_input):
        return oth.floor(float(re.search(floor_pattern, users_input).group(1)))

    if re.search(ceil_pattern, users_input):
        return oth.ceil(float(re.search(ceil_pattern, users_input).group(1)))

    else:
        return "Invalid input."


if __name__ == '__main__':
    while True:
        users_input = input("Enter your expression: ")
        preprocess(users_input)
