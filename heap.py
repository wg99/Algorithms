class Heap:

    def parent(self, i):
        return (i - 1) // 2
    
    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def max_heapify(self, A, i):
        l = self.left(i)
        r = self.right(i)
        largest = i
        if l < len(A) and A[l] > A[largest]:
            largest = l
        if r < len(A) and A[r] > A[largest]:
            largest = r
        if largest != i:
            A[i], A[largest] = A[largest], A[i]
            self.max_heapify(A, largest)


if __name__ == '__main__':
    hp = Heap()
    A = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
    hp.max_heapify(A, 1)
    print(A)