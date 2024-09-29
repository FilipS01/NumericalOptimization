# line_search.py
from abc import ABC, abstractmethod

class LineSearchMethod(ABC):
    @abstractmethod
    def calculate_step_size(self, func, x, direction, params):
        pass
