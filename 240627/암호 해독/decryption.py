class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.dummy = Node(-1)
        self.head = self.dummy
        self.tail = self.dummy

    def end(self):
        return self.tail

    def begin(self):
        return self.head

    def push_back(self, data):
        if self.begin() == self.end():
            new_data = Node(data)

            new_data.prev = self.head
            new_data.next = None
        else:
            new_data = Node(data)

            new_data.prev = self.tail.prev
            new_data.next = None

            self.tail.prev.next = new_data
            self.tail = new_data

    def push_front(self, data):
        if self.begin() == self.end():
            self.push_back(data)
        else:
            new_data = Node(data)

            new_data.prev = self.head
            new_data.next = self.head.next

            self.head.next.prev = new_data
            self.head.next = new_data

    def insert(self, node, data):
        if node == self.begin():
            self.push_front(data)
        elif node == self.end():
            self.push_back(data)
        else:
            new_data = Node(data)

            new_data.prev = node
            new_data.next = node.next

            node.next = new_node
            node.next.prev = new_node

    def delete(self, node):
        if node == self.end():
            node.prev.next = None
            self.tail = node.prev
            # node.prev = None
            # node.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            # node.prev = None
            # node.next = None

        return node.prev

order = input()
dll = DLL()
print(order)
it = dll.head
for c in order:
    if c == '<':
        if it != dll.begin():
            it = it.prev
    elif c == '>':
        if it != dll.end():
            it = it.next
    elif c == '-':
        if it != dll.begin():
            it = dll.delete(it)
    else:
        dll.insert(it, c)

    it_ = dll.head
    ans = ''
    while it != dll.end():
        ans += it_.data
        it_.next

    print(ans)