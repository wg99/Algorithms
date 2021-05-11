"""Implementation of various order
statistic algorithms.
"""

import random

def minimum(lst):
    """Finds minimum element from
    a sequence.

    Input:
        lst: A sequence of numbers

    Runtime: O(N)
    """
    c_min = lst[0]
    for num in lst[1:]:
        if num < c_min:
            c_min = num
    return c_min


def main():
    """Main function for running tests
    of statistics functions.
    """
    lst = [random.randint(0, 1000) for i in range(200)]
    print(minimum(lst))
    print(min(lst) == minimum(lst))


if __name__ == "__main__":
    main()
