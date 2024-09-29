import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from Util.starting_point import starting_point_generator
from Util.optimization_parameters import OptimizationParameters
from main_controller import OptimizationController
from Util.evaluation_number import EvaluationNumbers

class OptimizationGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Numerical Optimization GUI")

        # Initialize Variables No
        self.initial_variables_no = 100  # Set initial to 100

        # Select Function
        self.function_label = tk.Label(root, text="Select Function:")
        self.function_label.grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
        self.function_dropdown = ttk.Combobox(root, values=["QF1", "QF2"])
        self.function_dropdown.grid(row=0, column=1, padx=10, pady=5)
        self.function_dropdown.bind("<<ComboboxSelected>>", self.update_starting_points)

        # Select Method Group
        self.method_group_label = tk.Label(root, text="Select Method Group:")
        self.method_group_label.grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
        self.method_group_dropdown = ttk.Combobox(root,
                                                  values=["ConjugateGradient", "GradientDescent", "ModifiedNewton",
                                                          "Newton", "QuasiNewton", "TrustRegion"])
        self.method_group_dropdown.grid(row=1, column=1, padx=10, pady=5)
        self.method_group_dropdown.bind("<<ComboboxSelected>>", self.update_method_options)

        # Select Method
        self.method_label = tk.Label(root, text="Select Method:")
        self.method_label.grid(row=4, column=0, sticky=tk.W, padx=10, pady=5)
        self.method_dropdown = ttk.Combobox(root)
        self.method_dropdown.grid(row=4, column=1, padx=10, pady=5)
        self.method_dropdown.bind("<<ComboboxSelected>>", self.update_line_search_params)



        # Starting Point
        self.starting_point_label = tk.Label(root, text="Starting Point:")
        self.starting_point_label.grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
        self.starting_point_entry = tk.Entry(root)
        self.starting_point_entry.grid(row=2, column=1, padx=10, pady=5)

        # Variables No
        self.variables_label = tk.Label(root, text="Variables No:")
        self.variables_label.grid(row=3, column=0, sticky=tk.W, padx=10, pady=5)
        self.variables_entry = tk.Entry(root)
        self.variables_entry.grid(row=3, column=1, padx=10, pady=5)
        self.variables_entry.insert(0, str(self.initial_variables_no))  # Set initial to 100

        # Line Search Params Container
        line_search_frame = tk.LabelFrame(root, text="Line Search Params", padx=10, pady=10)
        line_search_frame.grid(row=5, column=0, padx=10, pady=10, sticky="ew")

        self.line_search_label = tk.Label(line_search_frame, text="Select Line Search:")
        self.line_search_label.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.line_search_dropdown = ttk.Combobox(line_search_frame)
        self.line_search_dropdown.grid(row=0, column=1, padx=5, pady=5)

        # Line search parameters
        self.beta_label = tk.Label(line_search_frame, text="Beta:")
        self.beta_label.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.beta_entry = tk.Entry(line_search_frame)
        self.beta_entry.grid(row=1, column=1, padx=5, pady=5)

        self.start_point_label = tk.Label(line_search_frame, text="Start Point:")
        self.start_point_label.grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        self.start_point_entry = tk.Entry(line_search_frame)
        self.start_point_entry.grid(row=2, column=1, padx=5, pady=5)

        self.m_label = tk.Label(line_search_frame, text="M:")
        self.m_label.grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)
        self.m_entry = tk.Entry(line_search_frame)
        self.m_entry.grid(row=3, column=1, padx=5, pady=5)

        self.sigma_label = tk.Label(line_search_frame, text="Sigma:")
        self.sigma_label.grid(row=4, column=0, sticky=tk.W, padx=5, pady=5)
        self.sigma_entry = tk.Entry(line_search_frame)
        self.sigma_entry.grid(row=4, column=1, padx=5, pady=5)

        self.rho_label = tk.Label(line_search_frame, text="Rho:")
        self.rho_label.grid(row=5, column=0, sticky=tk.W, padx=5, pady=5)
        self.rho_entry = tk.Entry(line_search_frame)
        self.rho_entry.grid(row=5, column=1, padx=5, pady=5)

        # Function Value per Iteration Label
        self.function_plot_label = tk.Label(root, text="Function Value:")
        self.function_plot_label.grid(row=1, column=2, sticky=tk.W, padx=10, pady=5)

        # Plot for Function Value per Iteration
        self.function_fig = Figure(figsize=(5, 4), dpi=100)
        self.function_ax = self.function_fig.add_subplot(111)
        self.function_canvas = FigureCanvasTkAgg(self.function_fig, master=root)
        self.function_canvas.get_tk_widget().grid(row=5, column=2, padx=10, pady=5)

        # Gradient Value per Iteration Label
        self.gradient_plot_label = tk.Label(root, text="Gradient Value:")
        self.gradient_plot_label.grid(row=1, column=3, sticky=tk.W, padx=10, pady=5)

        # Plot for Gradient Value per Iteration
        self.gradient_fig = Figure(figsize=(5, 4), dpi=100)
        self.gradient_ax = self.gradient_fig.add_subplot(111)
        self.gradient_canvas = FigureCanvasTkAgg(self.gradient_fig, master=root)
        self.gradient_canvas.get_tk_widget().grid(row=5, column=3, padx=10, pady=5)

        # Stopping Condition Params Container
        stopping_condition_frame = tk.LabelFrame(root, text="Stopping Condition Params", padx=10, pady=10)
        stopping_condition_frame.grid(row=6, column=0, padx=10, pady=10, sticky="ew")

        self.max_iter_label = tk.Label(stopping_condition_frame, text="Max Iterations:")
        self.max_iter_label.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.max_iter_entry = tk.Entry(stopping_condition_frame)
        self.max_iter_entry.grid(row=0, column=1, padx=5, pady=5)
        self.max_iter_entry.insert(0, "1000")  # Set initial to 1000

        self.epsilon_label = tk.Label(stopping_condition_frame, text="Epsilon:")
        self.epsilon_label.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.epsilon_entry = tk.Entry(stopping_condition_frame)
        self.epsilon_entry.grid(row=1, column=1, padx=5, pady=5)
        self.epsilon_entry.insert(0, "1e-6")  # Set initial to 1e-6

        self.work_precision_label = tk.Label(stopping_condition_frame, text="Work Precision:")
        self.work_precision_label.grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        self.work_precision_entry = tk.Entry(stopping_condition_frame)
        self.work_precision_entry.grid(row=2, column=1, padx=5, pady=5)
        self.work_precision_entry.insert(0, "1e-16")  # Set initial to 1e-16

        # Results Container
        results_frame = tk.LabelFrame(root, text="Results", padx=10, pady=10)
        results_frame.grid(row=6, column=2, padx=10, pady=10, sticky="ew")

        self.method_result_label = tk.Label(results_frame, text="Method:")
        self.method_result_label.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.method_result_value = tk.Label(results_frame, text="")
        self.method_result_value.grid(row=0, column=1, padx=5, pady=5)

        self.function_result_label = tk.Label(results_frame, text="Function:")
        self.function_result_label.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.function_result_value = tk.Label(results_frame, text="")
        self.function_result_value.grid(row=1, column=1, padx=5, pady=5)

        self.fmin_label = tk.Label(results_frame, text="Fmin:")
        self.fmin_label.grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        self.fmin_entry = tk.Entry(results_frame)
        self.fmin_entry.grid(row=2, column=1, padx=5, pady=5)

        self.xmin_label = tk.Label(results_frame, text="Xmin:")
        self.xmin_label.grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)
        self.xmin_entry = tk.Entry(results_frame)
        self.xmin_entry.grid(row=3, column=1, padx=5, pady=5)

        self.iter_label = tk.Label(results_frame, text="Iterations:")
        self.iter_label.grid(row=4, column=0, sticky=tk.W, padx=5, pady=5)
        self.iter_entry = tk.Entry(results_frame)
        self.iter_entry.grid(row=4, column=1, padx=5, pady=5)

        self.grad_norm_label = tk.Label(results_frame, text="Gradient norm:")
        self.grad_norm_label.grid(row=5, column=0, sticky=tk.W, padx=5, pady=5)
        self.grad_norm_entry = tk.Entry(results_frame)
        self.grad_norm_entry.grid(row=5, column=1, padx=5, pady=5)

        self.f_eval_label = tk.Label(results_frame, text="Function eval no:")
        self.f_eval_label.grid(row=2, column=2, sticky=tk.W, padx=5, pady=5)
        self.f_eval_entry = tk.Entry(results_frame)
        self.f_eval_entry.grid(row=2, column=3, padx=5, pady=5)

        self.g_eval_label = tk.Label(results_frame, text="Gradient eval no:")
        self.g_eval_label.grid(row=3, column=2, sticky=tk.W, padx=5, pady=5)
        self.g_eval_entry = tk.Entry(results_frame)
        self.g_eval_entry.grid(row=3, column=3, padx=5, pady=5)

        self.hess_eval_label = tk.Label(results_frame, text="Hessian eval no:")
        self.hess_eval_label.grid(row=4, column=2, sticky=tk.W, padx=5, pady=5)
        self.hess_eval_entry = tk.Entry(results_frame)
        self.hess_eval_entry.grid(row=4, column=3, padx=5, pady=5)

        self.cpu_label = tk.Label(results_frame, text="CPU Time:")
        self.cpu_label.grid(row=5, column=2, sticky=tk.W, padx=5, pady=5)
        self.cpu_entry = tk.Entry(results_frame)
        self.cpu_entry.grid(row=5, column=3, padx=5, pady=5)

        # Add Find Minimum Button
        self.find_min_button = tk.Button(root, text="Find Minimum", command=self.on_find_minimum)
        self.find_min_button.grid(row=8, column=0, padx=10, pady=10)

    def update_starting_points(self, event):
        selected_function = self.function_dropdown.get()

        # Get dimension from "Variables No" text box
        try:
            dimension = int(self.variables_entry.get())
            if selected_function == "QF1":
                starting_point = starting_point_generator("QF1", dimension)
                self.starting_point_entry.delete(0, tk.END)
                self.starting_point_entry.insert(0, str(starting_point))
            elif selected_function == "QF2":
                starting_point = starting_point_generator("QF2", dimension)
                self.starting_point_entry.delete(0, tk.END)
                self.starting_point_entry.insert(0, str(starting_point))
        except ValueError:
            self.starting_point_entry.delete(0, tk.END)
            self.starting_point_entry.insert(0, "Invalid Dimension")

    def update_method_options(self, event):
        selected_method_group = self.method_group_dropdown.get()

        if selected_method_group == "ConjugateGradient":
            self.method_dropdown['values'] = ["CGMethod1", "CGMethod2"]
        elif selected_method_group == "GradientDescent":
            self.method_dropdown['values'] = ["GDMethod1", "GDMethod2", "GradientLineSearch"]
        elif selected_method_group == "ModifiedNewton":
            self.method_dropdown['values'] = ["GoldsteinPrice", "MNMethod2"]
        elif selected_method_group == "Newton":
            self.method_dropdown['values'] = ["NewtonMethod1", "NewtonMethod2"]
        elif selected_method_group == "QuasiNewton":
            self.method_dropdown['values'] = ["QNMethod1", "QNMethod2"]
        elif selected_method_group == "TrustRegion":
            self.method_dropdown['values'] = ["TRMethod1", "TRMethod2"]

        self.method_dropdown.current(0)  # Set first option selected

    def update_line_search_params(self, event):
        selected_method = self.method_dropdown.get()

        if selected_method == "GradientLineSearch":
            # Populate Line Search Dropdown and enable parameters
            self.line_search_dropdown['values'] = ["Armijo", "Goldstein", "Wolfe", "FixedStepSize"]
            self.line_search_dropdown.current(0)  # Default to first option

            self.beta_entry.config(state='normal')
            self.start_point_entry.config(state='normal')
            self.m_entry.config(state='normal')
            self.sigma_entry.config(state='normal')
            self.rho_entry.config(state='normal')

            # Optionally, set default values for the entries
            self.beta_entry.delete(0, tk.END)
            self.beta_entry.insert(0, "0.5")

            self.start_point_entry.delete(0, tk.END)
            self.start_point_entry.insert(0, "1.0")

            self.m_entry.delete(0, tk.END)
            self.m_entry.insert(0, "10")

            self.sigma_entry.delete(0, tk.END)
            self.sigma_entry.insert(0, "1e-4")

            self.rho_entry.delete(0, tk.END)
            self.rho_entry.insert(0, "0.1")
        else:
            # Reset line search dropdown and disable parameters
            self.line_search_dropdown['values'] = ["Armijo", "Goldstein", "Wolfe", "FixedStepSize"]
            self.line_search_dropdown.current(2)

            self.beta_entry.config(state='normal')
            self.start_point_entry.config(state='normal')
            self.m_entry.config(state='normal')
            self.sigma_entry.config(state='normal')
            self.rho_entry.config(state='normal')

            # Optionally, set default values for the entries
            self.beta_entry.delete(0, tk.END)
            self.beta_entry.insert(0, "0.8")

            self.start_point_entry.delete(0, tk.END)
            self.start_point_entry.insert(0, "1.0")

            self.m_entry.delete(0, tk.END)
            self.m_entry.insert(0, "10")

            self.sigma_entry.delete(0, tk.END)
            self.sigma_entry.insert(0, "0.9")

            self.rho_entry.delete(0, tk.END)
            self.rho_entry.insert(0, "0.0001")

    def on_find_minimum(self):
        # Collecting parameters from GUI
        variables_no = int(self.variables_entry.get())
        input_str = self.starting_point_entry.get().strip("[]")  # Remove brackets if they exist
        starting_point = [float(x) for x in input_str.split() if x]
        max_iterations = int(self.max_iter_entry.get())
        epsilon = float(self.epsilon_entry.get())
        work_precision = float(self.work_precision_entry.get())

        # Line Search parameters
        beta = float(self.beta_entry.get()) if self.beta_entry.get() else None
        sigma = float(self.sigma_entry.get()) if self.sigma_entry.get() else None
        rho = float(self.rho_entry.get()) if self.rho_entry.get() else None
        start_point = float(self.start_point_entry.get()) if self.start_point_entry.get() else None

        # Creating object params
        params = OptimizationParameters(
            variables_no=variables_no,
            starting_point=starting_point,
            max_iterations=max_iterations,
            epsilon=epsilon,
            work_precision=work_precision,
            beta=beta,
            sigma=sigma,
            rho=rho,
            start_point=start_point
        )

        # Calling function for finding minimum
        selected_function = self.function_dropdown.get()
        selected_method = self.method_dropdown.get()
        selected_line_search = self.line_search_dropdown.get()
        evaluation_numbers=EvaluationNumbers(0,0,0)

        xmin, fmin, iterations,function_values,gradient_values,grad_norm,evaluation_numbers,cpu_time = controller.find_minimum(selected_function, selected_method, selected_line_search,
                                                         params)

        # Updating results in GUI
        self.method_result_label.config(text=f"Method: {selected_method}")
        self.function_result_label.config(text=f"Function: {selected_function}")

        self.fmin_entry.delete(0, tk.END)
        self.fmin_entry.insert(0, fmin)

        self.xmin_entry.delete(0, tk.END)
        self.xmin_entry.insert(0, xmin)

        self.iter_entry.delete(0, tk.END)
        self.iter_entry.insert(0, iterations)

        self.grad_norm_entry.delete(0, tk.END)
        self.grad_norm_entry.insert(0, grad_norm)

        self.f_eval_entry.delete(0, tk.END)
        self.f_eval_entry.insert(0, evaluation_numbers.function_eval_no)

        self.g_eval_entry.delete(0, tk.END)
        self.g_eval_entry.insert(0, evaluation_numbers.gradient_eval_no)

        self.hess_eval_entry.delete(0, tk.END)
        self.hess_eval_entry.insert(0, evaluation_numbers.hessian_eval_no)

        self.cpu_entry.delete(0, tk.END)
        self.cpu_entry.insert(0, cpu_time)

        print(f"Fmin: {fmin}, Xmin: {xmin}, Iterations: {iterations}")


        # Visualization for Function Value

        self.function_ax.clear()
        self.function_ax.plot(function_values, linestyle='-', color='b')
        self.function_ax.set_title("Function Value")
        self.function_ax.set_xlabel("Iterations")
        self.function_ax.set_ylabel("Function")
        self.function_ax.grid(True)
        self.function_canvas.draw()  # Refreshing Plot

        # Visualization for Gradient Value

        self.gradient_ax.clear()
        self.gradient_ax.plot(gradient_values, linestyle='-', color='r')
        self.gradient_ax.set_title("Gradient Value")
        self.gradient_ax.set_xlabel("Iterations")
        self.gradient_ax.set_ylabel("Gradient")
        self.gradient_ax.grid(True)
        self.gradient_canvas.draw()  # Refreshing Plot


controller = OptimizationController()

if __name__ == "__main__":
    root = tk.Tk()
    app = OptimizationGUI(root)
    root.mainloop()