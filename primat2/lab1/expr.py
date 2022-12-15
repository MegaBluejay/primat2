import numpy as np
from scipy.optimize import linprog
from sympy import Expr, Le, init_printing, symbols

from .simplex import simplex

init_printing(use_unicode=True)

x1, x2, x3, x4, x5 = _x = symbols([f"x_{i}" for i in range(1, 6)])


def to_list(expr: Expr, n):
    return [float(expr.coeff(_x[i])) for i in range(n)]


def solve(ntest, n, objective, constraints, basic, direction="min"):
    f = np.array(to_list(objective, n))
    if direction != "min":
        f *= -1
    # a = np.array([to_list(constraint, n) for constraint in constraints])
    a = []
    ntot = n
    for constraint in constraints:
        if isinstance(constraint, Expr):
            row = to_list(constraint, n)
            row.extend([0] * (ntot - n))
            row.append(-float(constraint.as_coeff_Add()[0]))
        else:
            row = to_list(constraint.lhs, n)
            row.extend([0] * (ntot - n))
            row.append(1 if isinstance(constraint, Le) else -1)
            row.append(float(constraint.rhs))
            ntot += 1
        a.append(row)
    a = np.array(a)
    ans = simplex(a, f, np.array(basic) - 1)
    correct = linprog(f, A_eq=a[:, :-1], b_eq=a[:, -1]).x
    ok = ans is not None and np.allclose(ans, correct)
    if ans is None:
        ans = "unbounded"
    print(f"{ntest} {'OK' if ok else 'wrong'}: {ans}")
