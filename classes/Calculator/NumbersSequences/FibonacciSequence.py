from abc import ABC

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


if __name__ == '__main__':
    fib = FibonacciSequence()
    print(fib.get_range(3, 10))
