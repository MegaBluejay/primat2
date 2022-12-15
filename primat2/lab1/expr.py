import numpy as np
from sympy import Expr, init_printing, symbols

from .simplex import simplex

init_printing(use_unicode=True)

x1, x2, x3, x4, x5 = _x = symbols([f"x_{i}" for i in range(1, 6)])


def to_list(expr: Expr, n):
    coeffs = [expr.coeff(_x[i]) for i in range(n)]
    coeffs.append(expr.as_coeff_add()[0])
    return list(map(float, coeffs))


def solve(ntest, n, objective, constraints, basic, direction="min"):
    f = np.array(to_list(objective, n)[:-1])
    if direction != "min":
        f *= -1
    a = np.array([to_list(constraint, n) for constraint in constraints])
    a[:, -1] *= -1
    ans = simplex(a, f, np.array(basic) - 1)
    if ans is None:
        ans = "unbounded"
    print(f"{ntest}: {ans}")
