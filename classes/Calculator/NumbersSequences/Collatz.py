import os

import matplotlib.pyplot as plt


class Collatz:
    def __init__(self, n):
        self.n = n
        self.results = []

    def make_arr(self):
        num = self.n  # Kopiujemy wartość początkową do zmiennej lokalnej
        self.results.append(num)
        while num != 1:
            if num % 2:
                num = num * 3 + 1
            else:
                num = num // 2
            self.results.append(num)

    def get_interval(self):
        interval_string = ', '.join(str(num) for num in self.results)
        return interval_string

    def print_graph(self):
        self.make_arr()
        steps = list(range(len(self.results)))
        plt.plot(steps, self.results)
        plt.grid(True)
        plt.xlabel('Step')
        plt.ylabel('Value')
        plt.title('Collatz visualization')

        plot_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'visualization')
        os.makedirs(plot_directory, exist_ok=True)
        plt.savefig(os.path.join(plot_directory, 'collatz.png'))
        plt.show()
        plt.close()
