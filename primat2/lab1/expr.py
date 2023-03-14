import numpy as np
from scipy.optimize import linprog
from sympy import Expr, Le, symbols

from .simplex import full_simplex

x1, x2, x3, x4, x5 = _x = symbols([f"x_{i}" for i in range(1, 6)])


def to_list(expr: Expr, n):
    return [float(expr.coeff(_x[i])) for i in range(n)]


def convert(n, objective, constraints, direction):
    fog = np.array(to_list(objective, n))
    if direction != "min":
        fog *= -1
    ntot = n + sum(not isinstance(constraint, Expr) for constraint in constraints)
    f = np.hstack([fog, np.zeros(ntot - n)])

    q = 0
    a = []
    a_ub, b_ub, a_eq, b_eq = [], [], [], []
    for constraint in constraints:
        if isinstance(constraint, Expr):
            row = to_list(constraint, n)
            a_eq.append(row.copy())
            row.extend([0] * (ntot - n))
            b = -float(constraint.as_coeff_Add()[0])
            row.append(b)
            b_eq.append(b)
        else:
            row = to_list(constraint.lhs, n)
            if isinstance(constraint, Le):
                a_ub.append(row.copy())
            else:
                a_ub.append([-x for x in row])
            row.extend([0] * q)
            q += 1
            row.append(1 if isinstance(constraint, Le) else -1)
            row.extend([0] * (ntot - n - q))
            b = float(constraint.rhs)
            row.append(b)
            if isinstance(constraint, Le):
                b_ub.append(b)
            else:
                b_ub.append(-b)
        a.append(row)
    a = np.array(a)
    return fog, f, a, a_eq, b_eq, a_ub, b_ub


def solve1(n, objective, constraints, direction):
    _fog, f, a, *_rest = convert(n, objective, constraints, direction)
    return full_simplex(a, f)[:n]


def solve(ntest, n, objective, constraints, direction="min"):
    fog, f, a, a_eq, b_eq, a_ub, b_ub = convert(n, objective, constraints, direction)
    ans = full_simplex(a.copy(), f.copy())[:n]
    real_ans = linprog(
        fog,
        A_eq=np.array(a_eq) if a_eq else None,
        b_eq=np.array(b_eq) if b_eq else None,
        A_ub=np.array(a_ub) if a_ub else None,
        b_ub=np.array(b_ub) if b_ub else None,
    ).x
    print(ntest, round(np.sum(fog * ans), 5), round(np.sum(fog * real_ans), 5))
