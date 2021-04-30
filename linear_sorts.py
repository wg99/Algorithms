"""Implementations of various sorting algorithms that run in
linear time."""
import random

def counting_sort(lst, input_range):
    """Sort algorithm that takes a list and the range of possible
    inputs and sorts the list in linear time by first counting
    the occurences of each input and then using this information
    to correctly place each value in the output list.

    Runtime: O(N)

    Args:
        lst: A list of integers
        input_range: The upper limit for the value of the input
            integers. Lower limit currently set to 0.

    Returns: A sorted list of integers
    """
    target_lst = [0] * len(lst)
    temp_lst = [0] * (input_range + 1)

    for val in lst:
        temp_lst[val] += 1

    for i in range(len(temp_lst) - 1):
        temp_lst[i + 1] += temp_lst[i]

    for val in reversed(lst):
        target_lst[temp_lst[val] - 1] = val
        temp_lst[val] -= 1

    return target_lst


def counting_sort_tester():
    """Function for testing the counting_sort algorithm.
    """
    lst = [2, 5, 3, 0, 2, 3, 0, 3]
    print(lst)
    print(counting_sort(lst, 5))
    lst2 = [random.randint(0, 50) for i in range(20)]
    print(lst2)
    print(counting_sort(lst2, 50))


def main():
    """Main function for running sort tests.
    """
    counting_sort_tester()


if __name__ == '__main__':
    main()
