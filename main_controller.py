# main_controller.py
from Functions.quad_qf2 import quad_qf2
from LineSearch.line_search_factory import LineSearchFactory
from Methods.GradientDescent.gradient_descent import GradientLineSearch
from Functions.quad_qf1 import quad_qf1
from Functions.quad_qf2 import quad_qf2


class OptimizationController:
    def __init__(self):
        self.functions = {
            "QF1": quad_qf1,
            "QF2":quad_qf2,

        }
        self.methods = {
            "GradientLineSearch": GradientLineSearch
            # Dodaj druge metode
        }

    def find_minimum(self, selected_function, selected_method, selected_line_search, params):
        function = self.functions[selected_function]

        line_search_method = LineSearchFactory.create_line_search(selected_line_search)

        method = self.methods[selected_method](line_search_method)

        xmin, fmin, iterations, function_values,gradient_values,grad_norm,evaluation_numbers,cpu_time= method.find_minimum(function, params.starting_point, params.to_dict())

        return xmin, fmin, iterations, function_values,gradient_values,grad_norm,evaluation_numbers,cpu_time
