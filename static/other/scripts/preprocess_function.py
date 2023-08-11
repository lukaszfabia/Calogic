import re
import static.other.scripts.sketch_function as sf


def preprocess_function(data):
    pattern = r'(\d+)x'
    data = re.sub(pattern, r'\1*x', data)
    sf.plot_sketch_function(data)
    return data
