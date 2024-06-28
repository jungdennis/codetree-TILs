class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def pop(self):
        if self.empty():
            print('Empty Stack')
        else:
            return self.items.pop()

    def top(self):
        if self.empty():
            print('Empty Stack')
        else:
            return self.items[-1]


N = int(input())
stack = Stack()

for i in range(N):
    order = input()

    if 'push' in order:
        item = order.split()[-1]
        stack.push(item)
    elif 'pop' in order:
        print(stack.pop())
    elif 'size' in order:
        print(stack.size())
    elif 'empty' in order:
        print(int(stack.empty()))
    elif 'top' in order:
        print(stack.top())