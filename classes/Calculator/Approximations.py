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


def tanges(arg, limit):
    return sinus(arg, limit) / cosinus(arg, limit)


def cotanges(arg, limit):
    return inversion(tanges(arg, limit))


def secans(arg, limit):
    return inversion(cosinus(arg, limit))


def cosecans(arg, limit):
    return inversion(sinus(arg, limit))


def arcsinus(arg):
    return 0


def arccosinus(arg):
    return 0


def arctanges(arg):
    return 0


def arccotangens(arg):
    return 0


def natural_logarithm(arg, limit):
    return 0


def exponential(arg, limit):
    res = 0
    for i in range(limit):
        res += power(arg, i) / factorial(i)
    return res
