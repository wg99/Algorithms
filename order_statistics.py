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


def randomized_select(lst, i):
    def partition(left, right):
        pivot = lst[right]
        i = left - 1
        for j in range(left, right):
            if lst[j] <= pivot:
                i += 1
                lst[j], lst[i] = lst[i], lst[j]
        lst[i + 1], lst[right] = lst[right], lst[i + 1]
        return i + 1

    def randomized_partition(left, right):
        i = random.randint(left, right)
        lst[i], lst[right] = lst[right], lst[i]
        return partition(left, right)

    def randomized_select_helper(left, right, i):
        if left == right:
            return lst[left]
        pivot = randomized_partition(left, right)
        k = pivot - left + 1
        if i == k:
            return lst[pivot]
        elif i < k:
            return randomized_select_helper(left, pivot - 1, i)
        else:
            return randomized_select_helper(pivot + 1, right, i - k)

    return randomized_select_helper(0, len(lst) - 1, i)


def main():
    """Main function for running tests
    of order statistics functions.
    """
    lst = [random.randint(0, 1000) for i in range(20)]
    print(sorted(lst))
    print(randomized_select(lst, 1), min(lst))
    print(min(lst) == randomized_select(lst, 1))
    print(randomized_select(lst, 14), sorted(lst)[13])


if __name__ == "__main__":
    main()
