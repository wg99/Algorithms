"""Implementation of various sort algorithms with test cases.
"""

import random
import importlib

def insertion_sort(lst):
    """Sorts a list of integers from smallest to largest.

    Runtime: O(N^2)

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


def merge_sort(lst):
    """Sorts a list of integers from smallest to largest.

    Runtime: O(N*log(N))

    Args:
        lst: A list of integers.

    Returns:
        None
    """
    if len(lst) > 1:
        mid = len(lst) // 2
        llst, rlst = lst[:mid], lst[mid:]
        merge_sort(llst)
        merge_sort(rlst)
        i, j, k = 0, 0, 0
        while j < len(llst) or k < len(rlst):
            lval = llst[j] if j < len(llst) else float('inf')
            rval = rlst[k] if k < len(rlst) else float('inf')
            if lval <= rval:
                lst[i] = lval
                j += 1
            else:
                lst[i] = rval
                k += 1
            i += 1


def heap_sort(lst):
    """Runs heap sort algorithm contained in hand-written heap module.

    Runtime: O(N * log(N))

    Args:
        lst: A list of integers

    Returns:
        None
    """
    heap = importlib.import_module('heap')
    my_heap = heap.Heap(lst)
    my_heap.heap_sort()


def sort_tester(sort):
    """Function for testing sort methods.
    """
    def sort_test_helper(lst):
        print(lst)
        sort(lst)
        print(lst)

    sort_test_helper([11,14,16,9,15,20])
    sort_test_helper([4, 15, 12, 3, 10, 6])
    sort_test_helper([random.randint(0, 50) for i in range(15)])


def main():
    """Main function for testing various sort methods.
    """
    sort_tester(heap_sort)


if __name__ == '__main__':
    main()
