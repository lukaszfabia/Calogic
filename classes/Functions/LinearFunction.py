import re

from classes.Functions.ConstantFunction import ConstantFunction
from classes.Functions.Function import Function
from classes.Functions.PrintGraph import generate_plot


def parse_coefficient(group):
    if group is None or group == "":
        return 0
    elif group == "-":
        return -1
    else:
        return float(group)


class LinearFunction(Function):
    def __init__(self, function):
        super().__init__(function)
        self.a = None
        self.b = None
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

    def print_graph(self):
        generate_plot(self.get_function())

    def solve(self):
        if self.get_a() == 0:
            return "The function has no real roots"
        else:
            root = -self.get_b() / self.get_a()
            return f"The function has one real root: {root:.2f}"

    def derivative(self):
        return ConstantFunction(str(self.get_a()))

    def local_extreme(self):
        raise NotImplementedError()

    def __str__(self):
        return f"LinearFunction{{a={self.a}, b={self.b}}}"

    def calculate(self, x):
        return self.get_a() * x + self.get_b()

    def preprocess(self):
        function = re.sub(r"\s+", "", self.get_function())
        pattern = r"([+-]?\d*)x([+-]\d*)?"
        match = re.search(pattern, function)
        if match:
            self.set_a(parse_coefficient(match.group(1)))
            self.set_b(parse_coefficient(match.group(2)))
        else:
            raise ValueError("Function is not linear")


# Testing the LinearFunction class
if __name__ == "__main__":
    linear_function = LinearFunction("-3x-653")
    linear_function.print_graph()
