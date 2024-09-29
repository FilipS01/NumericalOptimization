# gradient_line_search.py
import time
import numpy as np
from Util.optimization_methods import OptimizationMethod
from Util.evaluation_number import EvaluationNumbers


class GradientLineSearch(OptimizationMethod):
    def __init__(self, line_search_method):
        self.line_search_method = line_search_method

    def find_minimum(self, function, starting_point, params):
        epsilon = params['epsilon']
        max_iter = params['max_iterations']
        work_precision = params['work_precision']

        evaluation_numbers = EvaluationNumbers()  # Kreiramo EvaluationNumbers objekat
        start_time = time.process_time()

        x = starting_point
        function_values = []  # Lista za čuvanje vrednosti funkcije
        gradient_values = []  # Lista za čuvanje vrednosti gradijenta
        prev_fx = None  # Da čuvamo prethodnu vrednost funkcije radi poređenja

        for it in range(max_iter):
            # Izračunaj funkcijsku vrednost, gradijent i eventualno hesijan
            fx, grad, _ = function(x, [1, 1, 0])
            evaluation_numbers.increment_by([1, 1, 0])  # 1 evaluacija funkcije i gradijenta, 0 hesijana

            function_values.append(fx)
            gradient_values.append(np.linalg.norm(grad))

            if np.linalg.norm(grad) < epsilon:
                break

            if prev_fx is not None and abs(prev_fx - fx) < work_precision:
                print(f"Zaustavljeno zbog male promene u vrednosti funkcije ({abs(prev_fx - fx)} < {work_precision})")
                break

            prev_fx = fx

            # Koristi Line Search metodu da dobiješ veličinu koraka i evaluacije
            direction = -grad
            step_size, line_search_evaluations = self.line_search_method.calculate_step_size(function, x, direction,
                                                                                             params)

            # Dodaj evaluacije iz Line Search metode
            evaluation_numbers += line_search_evaluations

            # Ažuriraj poziciju
            x = x + step_size * direction

        cpu_time = time.process_time() - start_time
        fmin, _, _ = function(x, [1, 1, 0])
        evaluation_numbers.increment_function_eval_no()  # Poslednja evaluacija funkcije
        grad_norm=gradient_values[it]
        # Vraćamo rezultate, uključujući evaluacije
        return x, fmin, it, function_values, gradient_values,grad_norm, evaluation_numbers,cpu_time
