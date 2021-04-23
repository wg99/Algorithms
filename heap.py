class Heap:

    def __init__(self, array):
        self.array = array

    def parent(self, i): 
        return (i - 1) // 2
    
    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2


if __name__ == '__main__':
    hp = Heap([16,14,10,8,7,9,3,2,4,1])
    print(hp.array)
    print(hp.parent(2))
    print(hp.array[hp.right(3)])