import numpy as np


def simplex(a, f, basic):
    n, m = a.shape
    for i, j in enumerate(basic):
        a[i] /= a[i, j]
        for k in range(n):
            if k != i:
                a[k] -= a[i] * a[k, j]
        f -= a[i, :-1] * f[j]
    while True:
        j = np.argmin(f)
        if f[j] >= 0:
            break
        col = np.ma.masked_less_equal(a[:, j], 0, copy=False)
        i = np.argmin(a[:, -1] / col)
        if a[i, j] <= 0:
            return None
        basic[i] = j
        a[i] /= a[i, j]
        for k in range(n):
            if k != i:
                a[k] -= a[i] * a[k, j]
        f -= a[i, :-1] * f[j]
    ans = np.zeros(m - 1)
    ans[basic] = a[:, -1]
    return ans
