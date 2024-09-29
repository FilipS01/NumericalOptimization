# quad_qf1.py
import numpy as np

def quad_qf1(x, VGH):
    n = len(x)
    outVal = 0.0
    outGr = np.zeros(n)
    outHes = 0

    if VGH[0] > 0:
        outVal = 0.5 * sum(i * x[i] ** 2 for i in range(n)) - x[-1]

    if VGH[1] > 0:
        outGr = np.array([i * x[i] for i in range(n)])
        outGr[-1] -= 1

    if VGH[2] > 0:
        outHes = np.diag(np.arange(1, n + 1))

    return outVal, outGr, outHes
