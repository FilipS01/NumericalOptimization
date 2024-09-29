class EvaluationNumbers:

    def __init__(self, function_eval_no=0, gradient_eval_no=0, hessian_eval_no=0):
        self.function_eval_no = function_eval_no
        self.gradient_eval_no = gradient_eval_no
        self.hessian_eval_no = hessian_eval_no

    def __add__(self, other):

        return EvaluationNumbers(
            self.function_eval_no + other.function_eval_no,
            self.gradient_eval_no + other.gradient_eval_no,
            self.hessian_eval_no + other.hessian_eval_no
        )

    def __sub__(self, other):

        return EvaluationNumbers(
            self.function_eval_no - other.function_eval_no,
            self.gradient_eval_no - other.gradient_eval_no,
            self.hessian_eval_no - other.hessian_eval_no
        )

    def __eq__(self, other):

        return (self.function_eval_no == other.function_eval_no and
                self.gradient_eval_no == other.gradient_eval_no and
                self.hessian_eval_no == other.hessian_eval_no)

    def increment_function_eval_no(self):

        self.function_eval_no += 1

    def decrement_function_eval_no(self):

        self.function_eval_no -= 1

    def increment_gradient_eval_no(self):

        self.gradient_eval_no += 1

    def decrement_gradient_eval_no(self):

        self.gradient_eval_no -= 1

    def increment_hessian_eval_no(self):

        self.hessian_eval_no += 1

    def decrement_hessian_eval_no(self):

        self.hessian_eval_no -= 1

    def increment_by(self, function_gradient_hessian):

        self.function_eval_no += function_gradient_hessian[0]
        self.gradient_eval_no += function_gradient_hessian[1]
        self.hessian_eval_no += function_gradient_hessian[2]

    def display(self):

        return (f"Function evaluations: {self.function_eval_no}, "
                f"Gradient evaluations: {self.gradient_eval_no}, "
                f"Hessian evaluations: {self.hessian_eval_no}")
