import numpy as np
from LineSearch.line_search import LineSearchMethod
from Util.evaluation_number import EvaluationNumbers  # Import EvaluationNumbers

class GoldsteinSearch(LineSearchMethod):
    def calculate_step_size(self, func, x, direction, params):
        evaluation_numbers = EvaluationNumbers()
        alpha = params['sigma']
        beta = params['beta']
        step = 1.0

        fx, grad, _ = func(x, [1, 1, 0])
        evaluation_numbers.increment_by([1, 1, 0])

        f_next = func(x + step * direction, [1, 0, 0])[0]
        evaluation_numbers.increment_by([1, 0, 0])

        while f_next > fx + alpha * step * np.dot(grad, direction):
            step *= beta
            f_next = func(x + step * direction, [1, 0, 0])[0]
            evaluation_numbers.increment_by([1, 0, 0])

        return step, evaluation_numbers
