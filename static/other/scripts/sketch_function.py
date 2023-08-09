import os

import numpy as np
import matplotlib.pyplot as plt
from sympy import sympify, symbols, lambdify


def plot_sketch_function(func_str):
    x = np.linspace(-10, 10, 1000)
    x_sym = symbols('x')
    func = sympify(func_str)
    func_num = lambdify(x_sym, func, 'numpy')
    y = func_num(x)
    plt.plot(x, y, 'b', label=f'${func}$')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.legend(loc='upper left')
    plot_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../images/plots')
    os.makedirs(plot_directory, exist_ok=True)
    plt.savefig(os.path.join(plot_directory, 'plot.png'))
    plt.show()
    plt.close()
