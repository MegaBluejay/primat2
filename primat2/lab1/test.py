from .expr import solve, x1, x2, x3, x4, x5

solve(
    ntest=1,
    n=4,
    objective=-6 * x1 - x2 - 4 * x3 + 5 * x4,
    constraints=[
        3 * x1 + x2 - x3 + x4 - 4,
        5 * x1 + x2 + x3 - x4 - 4,
    ],
    basic=[1, 4],
)

solve(
    ntest=2,
    n=4,
    objective=-x1 - 2 * x2 - 3 * x3 + x4,
    constraints=[
        x1 - 4 * x2 - x3 - 2 * x4 + 4,
        x1 - x2 + x3,
    ],
    basic=[2, 3],
)

solve(
    ntest=3,
    n=5,
    objective=-x1 - 2 * x2 - x3 + 3 * x4 - x5,
    constraints=[
        x1 + x2 + 2 * x4 + x5 - 5,
        x1 + x2 + x3 + 3 * x4 + 2 * x5 - 9,
        x2 + x3 + 2 * x4 + x5 - 6,
    ],
    basic=[3, 4, 5],
)

solve(
    ntest=4,
    n=5,
    objective=-x1 - x2 - x3 + x4 - x5,
    constraints=[
        x1 + x2 + 2 * x3 - 4,
        -2 * x2 - 2 * x3 + x4 - x5 + 6,
        x1 - x2 + 6 * x3 + x4 + x5 - 12,
    ],
    basic=[1, 2, 3],
)

# solve(
#     ntest=5,
#     n=4,
#     objective=-x1 + 4 * x2 - 3 * x3 + 10 * x4,
#     constraints=[
#         x1 + x2 - x3 - 10 * x4,
#         x1 + 14 * x2 + 10 * x3 - 10 * x4 - 11,
#     ],
# )
#
# solve(
#     ntest=6,
#     n=4,
#     objective=-x1 + 5 * x2 + x3 - x4,
#     constraints=[
#         x1 + 3 * x2 + 3 * x3 + x4 <= 3,
#         2 * x1 + 3 * x3 - x4 <= 4,
#     ],
# )
#
# solve(
#     ntest=7,
#     n=5,
#     objective=-x1 - x2 + x3 - x4 + 2 * x5,
#     constraints=[
#         3 * x1 + x2 + x3 + x4 - 2 * x5 - 10,
#         6 * x1 + x2 + 2 * x3 + 3 * x4 - 4 * x5 - 20,
#         10 * x1 + x2 + 3 * x3 + 6 * x4 - 7 * x5 - 30,
#     ],
# )
