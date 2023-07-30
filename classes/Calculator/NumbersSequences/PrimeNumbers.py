from abc import ABC

from classes.Calculator.NumbersSequences.SequenceBeLike import SequenceBeLike


def is_prime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False

    return True


class PrimeNumbers(SequenceBeLike, ABC):
    def __init__(self):
        super().__init__()

    def get_value(self, index):
        return 0

    def get_range(self, begin, end):
        result=[]
        for i in range(begin, end+1):
            if is_prime(i):
                result.append(str(i))
        return ' '.join(result)
