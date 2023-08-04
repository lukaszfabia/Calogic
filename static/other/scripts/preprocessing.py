import re
import classes.Calculator.Other as oth
import classes.Calculator.Approximations as apprx


def preprocess(users_input):
    factorial_pattern = r"([+]?\d*)!"  # pattern for factorial
    power_pattern = r"([+]?\d*)\^([+]?\d*)"  # pattern for power
    square_root_pattern = r"sqrt\((\d+(\.\d+)?)\)"  # pattern for square root
    absolute_value_pattern = r"\|(-?\d+(\.\d+)?)\|"  # pattern for absolute value
    cube_root_pattern = r"cbrt\((-?\d+(\.\d+)?)\)"  # pattern for cube root
    inversion_pattern = r"1/(-?\d+(\.\d+)?)"  # pattern for inversion
    floor_pattern = r"floor\((-?\d+(\.\d+)?)\)"  # pattern for floor
    ceil_pattern = r"ceil\((-?\d+(\.\d+)?)\)"  # pattern for ceil
    n_root_pattern1 = r"nrt\((-?\d+(\.\d+)?),(\d+(\.\d+)?)\)"  # pattern for n root
    n_root_pattern2 = r"nrt\((-?\d+(\.\d+)?), (\d+(\.\d+)?)\)"  # pattern for n root

    pattern_for_sin = r"sin\((-?\d+(\.\d+)?)\)"  # pattern for sin
    pattern_for_cos = r"cos\((-?\d+(\.\d+)?)\)"  # pattern for cos
    pattern_for_tan = r"tan\((-?\d+(\.\d+)?)\)"  # pattern for tan
    pattern_for_cot = r"cot\((-?\d+(\.\d+)?)\)"  # pattern for cot
    pattern_for_sec = r"sec\((-?\d+(\.\d+)?)\)"  # pattern for sec
    pattern_for_csc = r"csc\((-?\d+(\.\d+)?)\)"  # pattern for csc
    pattern_for_ln = r"ln\((-?\d+(\.\d+)?)\)"  # pattern for ln
    pattern_for_arcsin = r"arcsin\((-?\d+(\.\d+)?)\)"  # pattern for arcsin
    pattern_for_arccos = r"arccos\((-?\d+(\.\d+)?)\)"  # pattern for arccos
    pattern_for_arctan = r"arctan\((-?\d+(\.\d+)?)\)"  # pattern for arctan
    pattern_for_arccot = r"arccot\((-?\d+(\.\d+)?)\)"  # pattern for arccot
    pattern_for_exponent = r"e\^(-?\d+(\.\d+)?)"  # pattern for exponent

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

    if re.search(n_root_pattern1, users_input):
        return oth.root(float(re.search(n_root_pattern1, users_input).group(1)),
                        int(re.search(n_root_pattern1, users_input).group(3)))

    if re.search(n_root_pattern2, users_input):
        return oth.root(float(re.search(n_root_pattern2, users_input).group(1)),
                        int(re.search(n_root_pattern2, users_input).group(3)))

    if re.search(pattern_for_sin, users_input):
        return apprx.sinus(float(re.search(pattern_for_sin, users_input).group(1)), 100)

    if re.search(pattern_for_cos, users_input):
        return apprx.cosinus(float(re.search(pattern_for_cos, users_input).group(1)), 100)

    if re.search(pattern_for_tan, users_input):
        return apprx.tangens(float(re.search(pattern_for_tan, users_input).group(1)), 100)

    if re.search(pattern_for_cot, users_input):
        return apprx.cotangens(float(re.search(pattern_for_cot, users_input).group(1)), 100)

    if re.search(pattern_for_sec, users_input):
        return apprx.secans(float(re.search(pattern_for_sec, users_input).group(1)), 100)

    if re.search(pattern_for_csc, users_input):
        return apprx.cosecans(float(re.search(pattern_for_csc, users_input).group(1)), 100)

    if re.search(pattern_for_ln, users_input):
        return apprx.natural_logarithm(float(re.search(pattern_for_ln, users_input).group(1)), 100)

    if re.search(pattern_for_arcsin, users_input):
        return apprx.arcsinus(float(re.search(pattern_for_arcsin, users_input).group(1)), 100)

    if re.search(pattern_for_arccos, users_input):
        return apprx.arccosinus(float(re.search(pattern_for_arccos, users_input).group(1)), 100)

    if re.search(pattern_for_arctan, users_input):
        return apprx.arctangens(float(re.search(pattern_for_arctan, users_input).group(1)), 100)

    if re.search(pattern_for_arccot, users_input):
        return apprx.arccotangens(float(re.search(pattern_for_arccot, users_input).group(1)), 100)

    if re.search(pattern_for_exponent, users_input):
        return apprx.exponential(float(re.search(pattern_for_exponent, users_input).group(1)), 100)
    else:
        return "Invalid input."