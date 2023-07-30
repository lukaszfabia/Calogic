from classes.Calculator.Other import factorial


def calculate_pi(limit):
    result = 0.0
    sign = 1.0
    for curr in range(1, limit + 1):
        result += sign / (2 * curr - 1)
        sign = -sign
    return result


def calculate_e(limit):
    result = 0.0
    for curr in range(limit + 1):
        result += 1 / factorial(curr)
    return result


def calculate_phi(limit):
    result = 1.0
    for curr in range(1, limit + 1):
        result = 1 + 1 / result
    return result


def phi():
    return calculate_phi(1000)


def e():
    return calculate_e(10)


def pi():
    return 4 * calculate_pi(1000)
