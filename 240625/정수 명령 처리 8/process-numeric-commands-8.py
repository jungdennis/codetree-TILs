class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.node_num = 0

    def push_front(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        new_node.prev = None

        if self.head != None:
            self.head.prev = new_node
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node

        self.node_num += 1

    def push_back(self, new_data):
        new_node = Node(new_data)
        new_node.next = None
        new_node.prev = self.tail

        if self.tail != None:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node

        self.node_num += 1

    def pop_front(self):
        if self.head == None:
            print('Empty DLL')
        elif self.head.next == None:
            temp = self.head

            self.head = None
            self.tail = None
            self.node_num = 0

            return temp.data
        else:
            temp = self.head

            temp.next.prev = None
            self.head = temp.next
            temp.next = None
            self.node_num -= 1

            return temp.data

    def pop_back(self):
        if self.tail == None:
            print('Empty DLL')
        elif self.tail.prev == None:
            temp = self.tail
            
            self.head = None
            self.tail = None
            self.node_num = 0

            return temp.data
        else:
            temp = self.tail

            temp.prev.next = None
            self.tail = temp.prev
            temp.prev = None
            self.node_num -= 1

            return temp.data
    
    def size(self):
        return self.node_num

    def empty(self):
        return self.node_num == 0

    def front(self):
        if self.head == None:
            print("Empty DLL")
        else:
            return self.head.data

    def back(self):
        if self.tail == None:
            print("Empty DLL")
        else:
            return self.tail.data

ans = DLL()
N = int(input())

for i in range(N):
    order = input()

    if 'push_front' in order:
        A = int(order.split()[-1])
        ans.push_front(A)
    elif 'push_back' in order:
        A = int(order.split()[-1])
        ans.push_back(A)
    elif 'pop_front' in order:
        print(ans.pop_front())
    elif 'pop_back' in order:
        print(ans.pop_back())
    elif 'size' in order:
        print(ans.size())
    elif 'empty' in order:
        print(int(ans.empty()))
    elif 'front' in order:
        print(ans.front())
    elif 'back' in order:
        print(ans.back())