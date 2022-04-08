import math


def distance(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])


def norm_2D(v):
    return math.hypot(v[0], v[1])  # fastest 2D norm in the west
