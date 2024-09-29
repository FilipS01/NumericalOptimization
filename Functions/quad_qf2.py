import numpy as np

def quad_qf2(x0, VGH):
    n = len(x0)
    outVal = 0.0
    outGr = np.zeros(n)

    c = 0.5

    if VGH[0] > 0:
        outVal = c * sum((i + 1) * (x0[i] ** 2 - 1) ** 2 for i in range(n)) - x0[-1]

    if VGH[1] > 0:
        for i in range(n):
            outGr[i] = 4 * c * (i + 1) * x0[i] * (x0[i] ** 2 - 1)
        outGr[-1] -= 1

    if VGH[2] > 0:
        outHes = np.zeros((n, n))
        for i in range(n):
            outHes[i, i] = 12 * c * (i + 1) * x0[i] ** 2 - 4 * c * (i + 1)
    else:
        outHes = 0

    return outVal, outGr, outHes

