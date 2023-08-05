def power(n, deg):
    result = 1
    while deg > 0:
        result *= n
        deg -= 1
    return result


def square_root(n):
    return root(n, 2)


def cube_root(n):
    return root(n, 3)


def root(number, deg):
    if (number < 0 and deg % 2 == 0) or deg == 0:
        return "You can't calculate even root of negative number or root of 0."

    x0 = number
    precision = 1e-10
    max_iterations = 1000

    for i in range(max_iterations):
        x1 = (1.0 / deg) * ((deg - 1) * x0 + number / power(x0, deg - 1))  # Newton-Raphson formula
        if abs(x1 - x0) < precision:
            return x1
        x0 = x1

    return "Can't calculate root."


def absolute_value(n):
    return -n if n < 0 else n


def floor(n):
    return int(n)


def ceil(n):
    return int(n) + 1


def factorial(n):
    return 1 if n == 1 or n == 0 else n * factorial(n - 1)


def inversion(n):
    return None if n == 0 else 1 / n
