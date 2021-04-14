"""Implementation of insertion sort algorithm with test cases.
"""

import random


def insertion_sort(lst):
    """Sorts a list of integers from smallest to largest.

    Args:
        lst: A list of integers.

    Returns:
        None
    """
    for i in range(len(lst)):
        j = i
        key = lst[j]
        while j > 0 and key < lst[j - 1]:
            lst[j] = lst[j - 1]
            j -= 1
        lst[j] = key


def main():
    """Main function for testing insertion_sort method.
    """
    lst1 = [4, 15, 12, 3, 10, 6]
    print(lst1)
    insertion_sort(lst1)
    print(lst1)
    rand_lst = [random.randint(0, 50) for i in range(15)]
    print(rand_lst)
    insertion_sort(rand_lst)
    print(rand_lst)


if __name__ == '__main__':
    main()
