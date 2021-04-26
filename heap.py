"""Implementation of heap class from CLRS.
Implemented in support of a heap sort algorithm.
"""

class Heap:
    """Class that holds a heap data structure.
    Instance Variables:
        self.lst: A list of integers.
        self.heap_size: The number of elements in the heap.
    """

    def __init__(self, lst):
        self.lst = lst
        self.heap_size = len(lst)

    @classmethod
    def left(cls, i):
        """Returns the index of a node's left child.

        Arguments:
            i: Index to a node

        Returns:
            int: Integer representing the index of the left child.
        """
        return 2 * i + 1

    @classmethod
    def right(cls, i):
        """Returns the index of a node's right child.

        Arguments:
            i: Index to a node.

        Returns:
            int: Integer representing the index of the right child.
        """
        return 2 * i + 2

    def max_heapify(self, i):
        """Assumes binary trees at left(i) and right(i) are valid max_heaps,
        but self.lst[i] is smaller than one of its' children. Fixes this by
        moving value at self.lst[i] down so that subtree at index i becomes
        a valid max_heap.

        Arguments:
            i: Index to a node.

        Returns:
            None
        """
        left = Heap.left(i)
        right = Heap.right(i)
        largest = i
        if left < self.heap_size and self.lst[left] > self.lst[largest]:
            largest = left
        if right < self.heap_size and self.lst[right] > self.lst[largest]:
            largest = right
        if largest != i:
            self.lst[i], self.lst[largest] = self.lst[largest], self.lst[i]
            self.max_heapify(largest)

    def build_max_heap(self):
        """Converts self.lst to a max_heap by
        running the max_heapify function on all parent nodes.
        """
        mid_point = len(self.lst) // 2 - 1
        for i in range(mid_point, -1, -1):
            self.max_heapify(i)

    def heap_sort(self):
        """Runs heap_sort algorithm by continually extracting the largest
        element from the top of a max_heap and then running max_heapify to
        re-populate the top of the tree with the new largest element.

        Runtime: O(N * log(N))
        """
        self.build_max_heap()
        for i in range(len(self.lst) - 1, 0, -1):
            self.lst[0], self.lst[i] = self.lst[i], self.lst[0]
            self.heap_size -= 1
            self.max_heapify(0)
