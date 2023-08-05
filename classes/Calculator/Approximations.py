from math import log

from classes.Calculator.Other import power, factorial, inversion, square_root
import classes.Calculator.Constant as const


def sinus(arg, limit):
    rad = arg * const.pi() / 180
    res = 0
    for i in range(limit):
        res += power(-1, i) * power(rad, 2 * i + 1) / factorial(2 * i + 1)
    return res


def cosinus(arg, limit):
    rad = arg * const.pi() / 180
    res = 0
    for i in range(limit):
        res += power(-1, i) * power(rad, 2 * i) / factorial(2 * i)
    return res


def tangens(arg, limit):
    return sinus(arg, limit) / cosinus(arg, limit)


def cotangens(arg, limit):
    return inversion(tangens(arg, limit))


def secans(arg, limit):
    return inversion(cosinus(arg, limit))


def cosecans(arg, limit):
    return inversion(sinus(arg, limit))


def arcsinus(arg, limit):
    if arg < -1 or arg > 1:
        return "Argument must be in range [-1, 1]."

    res = 0
    for i in range(limit):
        res += factorial(2 * i) * power(arg, 2 * i + 1) / (power(4, i) * power(factorial(i), 2) * (2 * i + 1))
    return res


def arccosinus(arg, limit):
    if arg < -1 or arg > 1:
        return "Argument must be in range [-1, 1]."

    res = 0
    for i in range(0, limit):
        print(res)
        res += factorial(2 * i) * power(arg, 2 * i) / (power(4, i) * power(factorial(i), 2) * (2 * i + 1))
    return res


def arctangens(arg, limit):
    res = 0
    for i in range(limit):
        res += power(-1, i) * power(arg, 2 * i + 1) / (2 * i + 1)
    return res


def arccotangens(arg, limit):
    res = 0
    for i in range(limit):
        res += power(-1, i) * power(arg, 2 * i + 1) / (2 * i + 1)
    return const.pi() / 2 - res


def natural_logarithm(arg):
    return log(arg)


def logarithm(base, arg):
    return natural_logarithm(arg) / natural_logarithm(base)


def exponential(arg, limit):
    res = 0
    for i in range(limit):
        res += power(arg, i) / factorial(i)
    return res


if __name__ == '__main__':
    print(logarithm(2, 2))
