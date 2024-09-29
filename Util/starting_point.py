from Util.utility_functions import one_number, a_to_b, exp_array, rep_array

def starting_point_generator(function_name, initial_dimension):
    """Generates default starting points based on the selected function name."""
    starting_points = {}

    if function_name == 'QF1':
        # Generate a starting point for QF1, e.g., using one_number utility
        starting_points['QF1'] = one_number(1, initial_dimension)  # You can modify the parameters as needed
    elif function_name == 'QF2':
        # Generate a starting point for QF2
        starting_points['QF2'] = one_number(0.5, initial_dimension)  # You can modify the parameters as needed
    else:
        raise ValueError(f"Unknown function name: {function_name}")

    return starting_points[function_name]

# Example usage:
# initial_dimension = 3  # or any other dimension
# points = starting_point_generator('QF1', initial_dimension)
# print(points)
