import os
import re

import matplotlib.pyplot as plt
from sympy import symbols, sympify


def prepare_function(example):
    function = example
    # looking for a variable 'x'
    variable_match = re.search(r"[a-zA-Z]", function)
    if variable_match:
        variable_name = variable_match.group(0)
        function = re.sub(r"(?<!\w)(" + variable_name + r")", r"1*\1", function)
        function = re.sub(r"(\d)([a-zA-Z])", r"\1*\2", function)

    return function


def generate_plot(function_str):
    x = symbols('x')
    expr = sympify(prepare_function(function_str))

    x_vals = [-10 + i * 0.1 for i in range(201)]
    y_vals = [expr.subs(x, val) for val in x_vals]

    plt.plot(x_vals, y_vals)
    plt.axhline(y=0, color='black', linewidth=0.5)  # X-axis
    plt.axvline(x=0, color='black', linewidth=0.5)  # Y-axis
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('f(x)=' + function_str)
    plt.grid(True)
    plot_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'plots')

    # Create the directory if it doesn't exist
    os.makedirs(plot_directory, exist_ok=True)
    plt.savefig(os.path.join(plot_directory, 'generated_plot.png'))
    plt.show()
    plt.close()
