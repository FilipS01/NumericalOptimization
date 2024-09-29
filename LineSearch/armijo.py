import numpy as np
from LineSearch.line_search import LineSearchMethod
from Util.evaluation_number import EvaluationNumbers

class ArmijoSearch(LineSearchMethod):
    def calculate_step_size(self, func, x, direction, params):
        evaluation_numbers = EvaluationNumbers()
        beta = params['beta']
        sigma = params['sigma']
        step = 1.0


        fx, grad, _ = func(x, [1, 1, 0])
        evaluation_numbers.increment_by([1, 1, 0])


        while func(x + step * direction, [1, 0, 0])[0] > fx + sigma * step * np.dot(grad, direction):
            evaluation_numbers.increment_function_eval_no()
            step *= beta


        return step, evaluation_numbers
