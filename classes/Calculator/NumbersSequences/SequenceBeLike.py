from abc import ABC, abstractmethod


class SequenceBeLike(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def get_value(self, index):
        pass

    @abstractmethod
    def get_range(self, begin, end):
        pass

    @abstractmethod
    def get_visualisation(self, begin, end, dot_size):
        pass
