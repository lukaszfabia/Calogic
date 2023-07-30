import os
from abc import ABC

from matplotlib import pyplot as plt

from classes.Calculator.NumbersSequences.SequenceBeLike import SequenceBeLike


class FibonacciSequence(SequenceBeLike, ABC):
    def __init__(self):
        super().__init__()

    def get_value(self, index):
        if index == 0:
            return 0
        elif index == 1:
            return 1

        prev, current = 0, 1
        for i in range(2, index + 1):
            prev, current = current, prev + current

        return current

    def get_range(self, begin, end):
        result_list = []
        for i in range(begin, end):
            result_list.append(str(self.get_value(i)))
        result = ' '.join(result_list)
        return result

    def get_visualisation(self, begin, end, dot_size):
        res = []
        for i in range(begin, end + 1):
            res.append(self.get_value(i))

        plt.plot(res)
        plt.xlabel('the nth term of the sequence')
        plt.ylabel('values')
        plt.title('Fibonacci visualization')
        plt.grid(True)

        plot_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'visualization')
        os.makedirs(plot_directory, exist_ok=True)
        plt.savefig(os.path.join(plot_directory, 'fib.png'))
        plt.show()
        plt.close()
