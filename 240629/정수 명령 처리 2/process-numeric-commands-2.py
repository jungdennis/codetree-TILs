from collections import deque
import sys

class Queue:
    def __init__(self):
        self.dq = deque()

    def push(self, item):
        self.dq.append(item)

    def empty(self):
        return len(self.dq) == 0
    
    def size(self):
        return len(self.dq)

    def pop(self):
        if self.empty():
            print("Empty Queue")
        
        return self.dq.popleft()

    def front(self):
        if self.empty():
            print('Empty Queue')
        
        return self.dq[0]
    
N = int(sys.stdin.readline().rstrip())
queue = Queue()

for i in range(N):
    order = sys.stdin.readline().rstrip()

    if 'push' in order:
        A = order.split()[-1]
        queue.push(A)
    elif 'pop' in order:
        print(queue.pop())
    elif 'size' in order:
        print(queue.size())
    elif 'empty' in order:
        print(int(queue.empty()))
    elif 'front' in order:
        print(queue.front())