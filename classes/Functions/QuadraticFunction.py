import re
import math

from classes.Functions.Function import Function
from classes.Functions.LinearFunction import LinearFunction
from classes.Functions.PrintGraph import generate_plot


def parse_coefficient(coefficient_string):
    if not coefficient_string:
        return 1.0
    elif coefficient_string == "-":
        return -1.0
    else:
        try:
            return float(coefficient_string)
        except ValueError:
            return 0.0


def parsing_for_c(coefficient_string):
    try:
        return float(coefficient_string)
    except ValueError:
        return 0.0


class QuadraticFunction(Function):
    def __init__(self, function):
        super().__init__(function)
        self.a = None
        self.b = None
        self.c = None
        self.preprocess()

    def get_function(self):
        return self.function

    def get_a(self):
        return self.a

    def set_a(self, a):
        self.a = a

    def get_b(self):
        return self.b

    def set_b(self, b):
        self.b = b

    def get_c(self):
        return self.c

    def set_c(self, c):
        self.c = c

    def print_graph(self):
        generate_plot(self.get_function())

    def solve(self):
        if self.get_a() != 0:
            delta = self.get_b() ** 2 - 4 * self.get_a() * self.get_c()
            if delta == 0:
                root = -self.get_b() / (2 * self.get_a())
                if root == 0:
                    return "The function has one real root: 0.0"
                return f"The function has one real root: {root:.2f}"
            elif delta > 0:
                x1 = (-self.get_b() - math.sqrt(delta)) / (2 * self.get_a())
                x2 = (-self.get_b() + math.sqrt(delta)) / (2 * self.get_a())
                if x1 == 0:
                    return f"The function has two real roots: 0.0 and {x2:.2f}"
                if x2 == 0:
                    return f"The function has two real roots: {x1:.2f} and 0.0"
                return f"The function has two real roots: {x1:.2f} and {x2:.2f}"
            else:
                return "The function has no real roots."
        else:
            root = -self.get_c() / self.get_b()
            return f"The function has one real root: {root:.2f}"

    def derivative(self):
        if self.get_b() < 0:
            return LinearFunction(f"{2 * self.get_a():.2f}x - {abs(self.get_b()):.2f}")
        else:
            return LinearFunction(f"{2 * self.get_a():.2f}x + {self.get_b():.2f}")

    def local_extreme(self):
        max_arg = -self.get_b() / (2 * self.get_a())
        max_val = self.calculate(max_arg)
        if self.get_a() > 0:
            return f"The function has a local minimum at x = {max_arg:.2f} and y = {max_val:.2f}"
        else:
            return f"The function has a local maximum at x = {max_arg:.2f} and y = {max_val:.2f}"

    def __str__(self):
        return f"QuadraticFunction{{a={self.a}, b={self.b}, c={self.c}}}"

    def calculate(self, x):
        return self.get_a() * x ** 2 + self.get_b() * x + self.get_c()

    def preprocess(self):
        function = re.sub(r"\s+", "", self.get_function())
        pattern = r"([+-]?\d*)x\^2([+-]\d*)x([+-]\d*)"
        pattern_without_b = r"([+-]?\d*)x\^2([+-]\d*)"
        match = re.search(pattern, function)
        match_without_b = re.search(pattern_without_b, function)

        if match:
            self.set_a(parse_coefficient(match.group(1)))
            self.set_b(parse_coefficient(match.group(2)))
            self.set_c(parsing_for_c(match.group(3)))

        elif match_without_b:
            self.set_a(parse_coefficient(match_without_b.group(1)))
            self.set_b(0.0)
            self.set_c(parsing_for_c(match_without_b.group(2)))
        else:
            raise ValueError("Invalid function format. Please provide a quadratic function (ax^2 + bx + c).")


# Testing the QuadraticFunction class
if __name__ == "__main__":
    quadratic_function = QuadraticFunction("12x^2 - 3")
    quadratic_function.print_graph()
