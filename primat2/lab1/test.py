from .expr import solve, x

solve(
    n=4,
    objective=-6 * x[1] - x[2] - 4 * x[3] + 5 * x[4],
    constraints=[
        3 * x[1] + x[2] - x[3] + x[4] - 4,
        5 * x[1] + x[2] + x[3] - x[4] - 4,
    ],
    basic=[0, 3],
)
