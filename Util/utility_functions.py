import numpy as np

def one_number(number, dimension):
    """Returns an array of 'number' repeated 'dimension' times."""
    return np.full(dimension, number)

def a_to_b(a, b):
    """Returns an array of integers from 'a' to 'b'."""
    return np.arange(a, b + 1)

def exp_array(dimension, exp):
    """Returns an array of 'i^exp' for i in range from 1 to 'dimension'."""
    return np.array([round(i**exp, 5) for i in range(1, dimension + 1)])

def rep_array(dimension, *args):
    """Returns an array with repeated provided elements of length 'dimension'."""
    if args:
        aux = np.array(args)
        repeat_count = dimension // len(aux) + 1
        sp = np.tile(aux, repeat_count)[:dimension]
        return sp
    else:
        return np.zeros(dimension)

# Add more utility functions as needed
