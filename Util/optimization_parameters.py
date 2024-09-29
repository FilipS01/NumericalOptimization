# optimization_parameters.py
class OptimizationParameters:
    def __init__(self, variables_no, starting_point, max_iterations, epsilon, work_precision, beta=None, sigma=None,
                 rho=None,start_point=None, step_size=None):
        # Parametri za funkciju
        self.variables_no = variables_no
        self.starting_point = starting_point

        # Parametri za metodu
        self.max_iterations = max_iterations
        self.epsilon = epsilon
        self.work_precision = work_precision


        self.beta = beta
        self.sigma = sigma
        self.rho = rho
        self.start_point=start_point


    def to_dict(self):
        return {
            'variables_no': self.variables_no,
            'starting_point': self.starting_point,
            'max_iterations': self.max_iterations,
            'epsilon': self.epsilon,
            'work_precision': self.work_precision,
            'beta': self.beta,
            'sigma': self.sigma,
            'rho': self.rho,
            'start_point':self.start_point
        }
