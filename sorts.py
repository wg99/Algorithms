"""Implementation of insertion various algorithms with test cases.
"""

import random


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
        i, l, r = 0, 0, 0
        while l < len(llst) or r < len(rlst):
            lval = llst[l] if l < len(llst) else float('inf')
            rval = rlst[r] if r < len(rlst) else float('inf')
            if lval <= rval:
                lst[i] = lval
                l += 1
            else:
                lst[i] = rval
                r += 1
            i += 1

    
def sort_tester(sort):
    """Function for testing sort methods.
    """
    lst = [11,14,16,9,15,20]
    print(lst)
    sort(lst)
    print(lst)
    lst1 = [4, 15, 12, 3, 10, 6]
    print(lst1)
    sort(lst1)
    print(lst1)
    rand_lst = [random.randint(0, 50) for i in range(15)]
    print(rand_lst)
    sort(rand_lst)
    print(rand_lst)
    

def main():
    """Main function for testing various sort methods.
    """
    sort_tester(merge_sort)


if __name__ == '__main__':
    main()
