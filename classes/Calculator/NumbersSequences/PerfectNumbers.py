import os
from abc import ABC

from classes.Calculator.NumbersSequences.SequenceBeLike import SequenceBeLike
import matplotlib.pyplot as plt


def is_perfect(n):
    # 6 = 1 + 2 + 3
    sum = 0
    if n == 0:
        return False
    for i in range(1, n):
        if n % i == 0:
            sum += i

    return sum == n


class PerfectNumbers(SequenceBeLike, ABC):

    def __init__(self):
        super().__init__()

    def get_value(self, index):
        return NotImplemented("Unsupported method")

    def get_range(self, begin, end):
        res = []
        for i in range(begin, end + 1):
            if is_perfect(i):
                res.append(str(i))

        return ' '.join(res)

    def get_visualisation(self, begin, end, dot_size):
        res = []
        scale = list(range(-end, end*2))
        for i in range(begin, end + 1):
            if is_perfect(i):
                res.append(i)

        plt.scatter(res, res, marker='o', color='blue', s=dot_size)
        plt.xlabel('natural numbers')
        plt.ylabel('perfects')
        plt.title('Perfects visualization')
        x_padding = 5
        y_padding = 5
        plt.xlim(min(scale) - x_padding, max(scale) + x_padding)
        plt.ylim(min(scale) - y_padding, max(scale) + y_padding)

        plt.grid(True)

        plot_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'visualization')
        os.makedirs(plot_directory, exist_ok=True)
        plt.savefig(os.path.join(plot_directory, 'perfects.png'))
        plt.show()
        plt.close()

