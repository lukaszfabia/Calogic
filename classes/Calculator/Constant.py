from classes.Calculator.Other import factorial


def calculate_pi(limit, curr, sign):
    return 0.0 if curr > limit else sign / (2 * curr - 1) + calculate_pi(limit, curr + 1.0, -sign)


def calculate_e(limit, curr):
    return 0.0 if curr > limit else 1 / factorial(curr) + calculate_e(limit, curr + 1)


def calculate_phi(limit, curr):
    return 0.0 if curr > limit else 1 + 1 / calculate_phi(limit, curr + 1.0)


def phi():
    return calculate_phi(1000, 1.0)


def e():
    return calculate_e(10, 0)


def pi():
    return 4 * calculate_pi(1000, 1.0, 1.0)
