class Stack:
    def __init__(self):
        self.top = -1
        self.lst = []

    def stack_empty(self):
        if self.top == -1:
            return True
        return False
    
    def push(self, x):
        self.top += 1
        if self.top >= len(self.lst):
            self.lst.append(x)
        else:
            self.lst[self.top] = x

    def pop(self):
        if self.stack_empty():
            print("Error: Underflow")
        else:
            self.top -= 1
            return self.lst[self.top + 1]


def main():
    S = Stack()
    print(S.stack_empty)
    print(S.push(3))
    print(S.push(2))
    print(S.pop())
    print(S.push(4))
    print(S.pop())
    print(S.pop())


if __name__ == '__main__':
    main()