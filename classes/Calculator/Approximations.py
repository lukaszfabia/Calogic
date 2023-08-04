from classes.Calculator.Other import power, factorial, inversion


def sinus(arg, limit):
    res = 0
    for i in range(limit):
        res += power(-1, i) * power(arg, 2 * i + 1) / factorial(2 * i + 1)
    return res


def cosinus(arg, limit):
    res = 0
    for i in range(limit):
        res += power(-1, i) * power(arg, 2 * i) / factorial(2 * i)
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
    return 0


def arccosinus(arg, limit):
    return 0


def arctangens(arg, limit):
    return 0


def arccotangens(arg, limit):
    return 0


def natural_logarithm(arg, limit):
    return 0


def exponential(arg, limit):
    res = 0
    for i in range(limit):
        res += power(arg, i) / factorial(i)
    return res
