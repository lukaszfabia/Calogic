import os
from abc import ABC
import matplotlib.pyplot as plt
from classes.Calculator.NumbersSequences.SequenceBeLike import SequenceBeLike


def is_prime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):  # Optimized to check up to square root of n
        if n % i == 0:
            return False
    return True


class PrimeNumbers(SequenceBeLike, ABC):

    def __init__(self):
        super().__init__()

    def get_value(self, index):
        return NotImplemented("Unsupported method")

    def get_range(self, begin, end):
        res = []
        for i in range(max(2, begin), end + 1):  # Start from 2 to avoid negative numbers and optimize
            if is_prime(i):
                res.append(str(i))
        return ' '.join(res)

    def get_visualisation(self, begin, end, dot_size):
        res = []
        for i in range(begin, end + 1):
            if is_prime(i):
                res.append(i)

        plt.scatter(res, res, marker='o', color='blue', s=dot_size)
        plt.xlabel('natural numbers')
        plt.ylabel('primes')
        plt.title('Primes visualization')
        plt.grid(True)

        x_padding = 5
        y_padding = 5
        plt.xlim(min(res) - x_padding, max(res) + x_padding)
        plt.ylim(min(res) - y_padding, max(res) + y_padding)

        plot_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'visualization')
        os.makedirs(plot_directory, exist_ok=True)
        plt.savefig(os.path.join(plot_directory, 'primes.png'))
        plt.show()
        plt.close()

