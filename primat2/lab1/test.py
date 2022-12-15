from .expr import solve, x1, x2, x3, x4, x5

solve(
    n=4,
    objective=-6 * x1 - x2 - 4 * x3 + 5 * x4,
    constraints=[
        3 * x1 + x2 - x3 + x4 - 4,
        5 * x1 + x2 + x3 - x4 - 4,
    ],
    basic=[1, 4],
)

solve(
    n=4,
    objective=-x1 - 2 * x2 - 3 * x3 + x4,
    constraints=[
        x1 - 4 * x2 - x3 - 2 * x4 + 4,
        x1 - x2 + x3,
    ],
    basic=[2, 3],
)

solve(
    n=5,
    objective=-x1 - 2 * x2 - x3 + 3 * x4 - x5,
    constraints=[
        x1 + x2 + 2 * x4 + x5 - 5,
        x1 + x2 + x3 + 3 * x4 + 2 * x5 - 9,
        x2 + x3 + 2 * x4 + x5 - 6,
    ],
    basic=[3, 4, 5],
)
