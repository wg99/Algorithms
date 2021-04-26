class Heap:

    def __init__(self, A):
        self.A = A
        self.heap_size = len(A)

    def parent(self, i):
        return (i - 1) // 2
    
    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def max_heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        largest = i
        if l < self.heap_size and self.A[l] > self.A[largest]:
            largest = l
        if r < self.heap_size and self.A[r] > self.A[largest]:
            largest = r
        if largest != i:
            self.A[i], self.A[largest] = self.A[largest], self.A[i]
            self.max_heapify(largest)

    def build_max_heap(self):
        mid_point = len(self.A) // 2 - 1
        for i in range(mid_point, -1, -1):
            self.max_heapify(i)

    def heap_sort(self):
        self.build_max_heap()
        for i in range(len(self.A) - 1, 0, -1):
            self.A[0], self.A[i] = self.A[i], self.A[0]
            self.heap_size -= 1
            self.max_heapify(0)