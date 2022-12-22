import numpy as np


def simplex(a, f, basic):
    n, m = a.shape
    for i, j in enumerate(basic):
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
    return basic


def find_basic(a):
    n, m = a.shape
    basic_a = np.hstack([a[:, :-1], np.eye(n), a[:, -1:]])
    basic_f = np.zeros(m + n - 1)
    basic_f[-n:] = 1
    basic_basic = np.arange(m - 1, m + n - 1)
    basic = simplex(basic_a, basic_f, basic_basic)
    new_a = basic_a[:, np.r_[: m - 1, -1]]
    return new_a, basic


def full_simplex(a, f):
    a, basic = find_basic(a)
    basic = simplex(a, f, basic)
    ans = np.zeros_like(f)
    ans[basic] = a[:, -1]
    return ans
