import numpy as np
from sympy import Expr, IndexedBase

from .simplex import simplex

x = IndexedBase("x")


def to_list(expr: Expr, n):
    coeffs = [expr.coeff(x[i]) for i in range(1, n + 1)]
    coeffs.append(expr.as_coeff_add()[0])
    return coeffs


def solve(n, objective, constraints, basic, direction="min"):
    f = np.array(to_list(objective, n)[:-1])
    if direction != "min":
        f *= -1
    a = np.array([to_list(constraint, n) for constraint in constraints])
    basic = np.array(basic)
    ans = simplex(a, f, basic)
    if ans is None:
        ans = "unbounded"
    return ans
