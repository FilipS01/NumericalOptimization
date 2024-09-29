def compute_line_search_start_point(f_curr, f_prev, grad, dir):
    """
    Računa početnu tačku za linijsku pretragu prema ideji iz knjige
    Nocedal i Wright, 'Numerical Optimization', poglavlje 3, strana 58.

    Args:
        f_curr (float): Trenutna vrednost funkcije.
        f_prev (float): Prethodna vrednost funkcije.
        grad (np.array): Gradijent funkcije u trenutnoj tački.
        dir (np.array): Pravac pretrage.

    Returns:
        float: Početna tačka za linijsku pretragu.
    """
    import numpy as np

    ls_start_pnt = abs(2 * (f_curr - f_prev) / np.dot(dir, grad))
    return min(1, 1.01 * ls_start_pnt)



