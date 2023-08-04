import re
import classes.Calculator.Other as oth
import classes.Calculator.Approximations as apprx

limit = 30

patterns = {
    'factorial_pattern': r"([+]?\d*)!",
    'power_pattern': r"([+]?\d*)\^([+]?\d*)",
    'square_root_pattern': r"sqrt\((\d+(\.\d+)?)\)",
    'absolute_value_pattern': r"\|(-?\d+(\.\d+)?)\|",
    'cube_root_pattern': r"cbrt\((-?\d+(\.\d+)?)\)",
    'inversion_pattern': r"1/(-?\d+(\.\d+)?)",
    'floor_pattern': r"floor\((-?\d+(\.\d+)?)\)",
    'ceil_pattern': r"ceil\((-?\d+(\.\d+)?)\)",
    'n_root_pattern': r"nrt\((-?\d+(\.\d+)?), (\d+(\.\d+)?)\)",
    'sin_pattern': r"sin\((-?\d+(\.\d+)?)\)",
    'cos_pattern': r"cos\((-?\d+(\.\d+)?)\)",
    'tan_pattern': r"tan\((-?\d+(\.\d+)?)\)",
    'cot_pattern': r"cot\((-?\d+(\.\d+)?)\)",
    'sec_pattern': r"sec\((-?\d+(\.\d+)?)\)",
    'csc_pattern': r"csc\((-?\d+(\.\d+)?)\)",
    'ln_pattern': r"ln\((-?\d+(\.\d+)?)\)",
    'arcsin_pattern': r"arcsin\((-?\d+(\.\d+)?)\)",
    'arccos_pattern': r"arccos\((-?\d+(\.\d+)?)\)",
    'arctan_pattern': r"arctan\((-?\d+(\.\d+)?)\)",
    'arccot_pattern': r"arccot\((-?\d+(\.\d+)?)\)",
    'exp_pattern': r"e\^(-?\d*)"
}


def preprocess(users_input):
    for pattern_name, pattern in patterns.items():
        match = re.fullmatch(pattern, users_input)
        if match:
            if pattern_name == 'factorial_pattern':
                return oth.factorial(int(match.group(1)))
            elif pattern_name == 'power_pattern':
                return oth.power(int(match.group(1)), int(match.group(2)))
            elif pattern_name == 'square_root_pattern':
                return oth.square_root(int(match.group(1)))
            elif pattern_name == 'absolute_value_pattern':
                return oth.absolute_value(float(match.group(1)))
            elif pattern_name == 'cube_root_pattern':
                return oth.cube_root(int(match.group(1)))
            elif pattern_name == 'inversion_pattern':
                return oth.inversion(float(match.group(1)))
            elif pattern_name == 'floor_pattern':
                return oth.floor(float(match.group(1)))
            elif pattern_name == 'ceil_pattern':
                return oth.ceil(float(match.group(1)))
            elif pattern_name == 'n_root_pattern':
                return oth.root(float(match.group(1)), int(match.group(3)))
            elif pattern_name == 'sin_pattern':
                return apprx.sinus(float(match.group(1)), limit)
            elif pattern_name == 'cos_pattern':
                return apprx.cosinus(float(match.group(1)), limit)
            elif pattern_name == 'tan_pattern':
                return apprx.tangens(float(match.group(1)), limit)
            elif pattern_name == 'cot_pattern':
                return apprx.cotangens(float(match.group(1)), limit)
            elif pattern_name == 'sec_pattern':
                return apprx.secans(float(match.group(1)), limit)
            elif pattern_name == 'csc_pattern':
                return apprx.cosecans(float(match.group(1)), limit)
            elif pattern_name == 'ln_pattern':
                return apprx.natural_logarithm(float(match.group(1)), limit)
            elif pattern_name == 'arcsin_pattern':
                return apprx.arcsinus(float(match.group(1)), limit)
            elif pattern_name == 'arccos_pattern':
                return apprx.arccosinus(float(match.group(1)), limit)
            elif pattern_name == 'arctan_pattern':
                return apprx.arctangens(float(match.group(1)), limit)
            elif pattern_name == 'arccot_pattern':
                return apprx.arccotangens(float(match.group(1)), limit)
            elif pattern_name == 'exp_pattern':
                return apprx.exponential(float(match.group(1)), 15)

    return "Invalid input."

