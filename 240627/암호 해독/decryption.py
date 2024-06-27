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

    def push_back(self, data):
        if self.head == self.tail:
            new_data = Node(data)

            new_data.prev = self.head
            new_data.next = None

            self.head.next = new_data
            self.tail = new_data
        else:
            new_data = Node(data)

            new_data.prev = self.tail
            new_data.next = None

            self.tail.next = new_data
            self.tail = new_data

    def push_front(self, data):
        if self.head == self.tail:
            self.push_back(data)
        else:
            new_data = Node(data)

            new_data.prev = self.head
            new_data.next = self.head.next

            self.head.next.prev = new_data
            self.head.next = new_data

    def insert(self, node, data):
        if node == self.head:
            self.push_front(data)
        elif node == self.tail:
            self.push_back(data)
        else:
            new_data = Node(data)

            new_data.prev = node
            new_data.next = node.next

            node.next.prev = new_data
            node.next = new_data
            
    def delete(self, node):
        prev_node = node.prev

        if node == self.tail:
            node.prev.next = None
            self.tail = node.prev
            node.prev = None
            node.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            node.prev = None
            node.next = None

        return prev_node

order = input()
dll = DLL()
it = dll.head

for c in order:
    print(f"( {c} )")
    if c == '<':
        if it != dll.head:
            it = it.prev
    elif c == '>':
        if it != dll.tail:
            it = it.next
    elif c == '-':
        if it != dll.head:
            it = dll.delete(it)

            it_ = dll.head.next
            ans = ''
            while True:
                if it_ == dll.tail:
                    break
                ans += it_.data
                print(ans)
                it_.next
    else:
        dll.insert(it, c)

        it_ = dll.head.next
        ans = ''
        while True:
            if it_ == dll.tail:
                break
            ans += it_.data
            print(ans)
            it_.next