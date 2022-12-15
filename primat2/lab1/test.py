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
