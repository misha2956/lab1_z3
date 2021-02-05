"""
This project is created to compute square sides
"""

from math import tan, sqrt

def get_base_and_side_len(side_a: float, side_b: float, side_c: float) -> tuple:
    """
    This function finds side and base length of a triagle

    >>> get_base_and_side_len(2, 2, 3)
    (3, 2)
    """

    sides = {}

    for side in [side_a, side_b, side_c]:
        if side in sides:
            sides[side] += 1
        else:
            sides[side] = 1

    base, side = [
        key_val[0]
        for key_val in sorted(
            sides.items(), key=lambda key_val: key_val[1]
        )
    ]

    return base, side


def get_square_sides(
        side_a: float or int, side_b: float or int,
        side_c: float or int, epsilon: float
    ):
    """
    This function computes the solution to the problem

    >>> get_square_sides(5, 5, 6, 0.0001)
    0.978515625
    """

    base, side = get_base_and_side_len(side_a, side_b, side_c)

    x_min = 0
    x_max = base / 2

    side_lamb = lambda x: x * tan(sqrt(
        side ** 2 - (base / 2) ** 2
    ) / (
        base / 2
    ))

    opt_func = lambda x: side_lamb(x) - (base - x * 2)

    while True:

        mid = (x_max + x_min) / 2

        if abs(opt_func(mid)) < epsilon:
            return mid
        if opt_func(mid) > 0:
            x_max = mid
        else:
            x_min = mid


if __name__ == "__main__":
    import doctest
    doctest.testmod()
