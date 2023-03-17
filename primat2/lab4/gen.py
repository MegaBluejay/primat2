import numpy as np

rng = np.random.default_rng()


def generate(n):
    x = rng.uniform(-1, 1, (n, 2))
    y = x[:, 0] ** 2 + x[:, 1] ** 2 <= 0.25
    return x, y
