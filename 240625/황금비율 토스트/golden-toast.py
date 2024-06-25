class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.END = Node(-1)
        self.head = self.END
        self.tail = self.END

    def begin(self):
        return self.head

    def end(self):
        return self.tail

    def push_front(self, new_data):
        new_node = Node(new_data)

        new_node.next = self.head
        new_node.prev = None

        self.head.prev = new_node
        self.head = new_node

    def push_back(self, new_data):
        if self.begin() == self.end():
            self.push_front(new_data)
        else:
            new_node = Node(new_data)

            new_node.next = self.tail
            new_node.prev = self.tail.prev

            self.tail.prev.next = new_node
            self.tail.prev = new_node

    def erase(self, node):
        next_node = node.next

        if node == self.begin():
            temp = self.head

            temp.next.prev = None
            self.head = temp.next
            temp.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            node.prev = None
            node.next = None

        return next_node

    def insert(self, node, new_data):
        if node == self.begin():
            self.push_front(new_data)
        elif node == self.end():
            self.push_back(new_data)
        else:
            new_node = Node(new_data)
            
            new_node.prev = node.prev
            new_node.next = node

            node.prev.next = new_node
            node.prev = new_node

n, m = map(int, input().split())

dll = DLL()
initial = input()

for c in initial:
    dll.push_back(c)

it = dll.end()

for i in range(m):
    order = input()

    if 'L' == order[0]:
        if it != dll.begin():
            it = it.prev
    elif 'R' == order[0]:
        if it != dll.end():
            it = it.next
    elif 'D' == order[0]:
        dll.erase(it)
    elif 'P' == order[0]:
        c = order.split()[1]
        dll.insert(it, c)
    
ans = ''
it_ = dll.begin()
while it_ != dll.end():
    if it_.data != -1:
        ans += it_.data
    it_ = it_.next

print(ans)