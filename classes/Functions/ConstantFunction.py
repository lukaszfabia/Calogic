from classes.Functions.Function import Function
from classes.Functions.PrintGraph import generate_plot


class ConstantFunction(Function):
    def __init__(self, function):
        super().__init__(function)
        self.constant = None
        self.preprocess()

    def get_function(self):
        return self.function

    def get_constant(self):
        return self.constant

    def set_constant(self, constant):
        self.constant = constant

    def preprocess(self):
        if self.get_function()[0] != '-':
            self.set_constant(float(self.get_function()))
        else:
            self.set_constant(-float(self.get_function()[1:]))

    def print_graph(self):
        generate_plot(self.get_function())

    def solve(self):
        raise NotImplementedError()

    def derivative(self):
        return ConstantFunction("0")

    def local_extreme(self):
        return None

    def __str__(self):
        return f"ConstantFunction{{constant={self.constant}}}"

    def calculate(self, x):
        return self.get_constant()
