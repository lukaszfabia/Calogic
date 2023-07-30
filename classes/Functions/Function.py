from abc import ABC, abstractmethod


class Function(ABC):
    def __init__(self, function):
        if function is None or not function.strip():
            raise ValueError("Function cannot be empty or None")
        self.function = function

    @abstractmethod
    def print_graph(self):
        pass

    @abstractmethod
    def solve(self):
        pass

    @abstractmethod
    def derivative(self):
        pass

    @abstractmethod
    def local_extreme(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def calculate(self, x):
        pass
