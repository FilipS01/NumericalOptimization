import numpy as np
from LineSearch.line_search import LineSearchMethod
from Util.evaluation_number import EvaluationNumbers

class WolfeSearch(LineSearchMethod):
    def calculate_step_size(self, func, x, direction, params):
        evaluation_numbers = EvaluationNumbers()
        c1 = params['sigma']  # You can use sigma as c1
        c2 = params['rho']    # Assuming rho is for c2
        step = 1.0


        fx, grad, _ = func(x, [1, 1, 0])
        evaluation_numbers.increment_by([1, 1, 0])


        f_next = func(x + step * direction, [1, 0, 0])[0]
        grad_next = np.dot(func(x + step * direction, [1, 1, 0])[1], direction)
        evaluation_numbers.increment_by([1, 1, 0])

        while f_next > fx + c1 * step * np.dot(grad, direction):
            step *= 0.5
            f_next = func(x + step * direction, [1, 0, 0])[0]
            grad_next = np.dot(func(x + step * direction, [1, 1, 0])[1], direction)
            evaluation_numbers.increment_by([1, 1, 0])

        while grad_next < c2 * np.dot(grad, direction):
            step *= 2
            f_next = func(x + step * direction, [1, 0, 0])[0]
            grad_next = np.dot(func(x + step * direction, [1, 1, 0])[1], direction)
            evaluation_numbers.increment_by([1, 1, 0])

        return step, evaluation_numbers
