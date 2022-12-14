import numpy as np


def simplex(a):
    n = a.shape[0]
    while a[0, (j := np.argmin(a[0, :-1]))] < 0:
        ratio = a[1:-1, -1] / a[1:-1, j]
        i = np.ma.masked_less_equal(ratio, 0, copy=False).argmin() + 1
        if ratio[i] <= 0:
            return None
        a[i] /= a[i, j]
        for k in range(n):
            if k == i:
                continue
            a[i] -= a[i] * (a[k, j] / a[i, j])
    return
