import numpy as np

def triangular_membership(x, a, b, c):
    if x <= a or x >= c:
        return 0
    elif a < x < b:
        return (x - a) / (b - a)
    elif b <= x < c:
        return (c - x) / (c - b)

membership_low = triangular_membership(2, 0, 5, 10)
membership_medium = triangular_membership(5, 0, 5, 10)
membership_high = triangular_membership(8, 0, 5, 10)