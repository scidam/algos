# Stack implementation using linked list

class Node:
    def __init__(self, value):
        self.next = None
        self.value = value


class LinkedList:
    def __init__(self):
        self.root = None
        self.head = self.root

    def add(self, node):
        if self.root is None:
            self.root = node
            self.head = self.root
        else:
            node.next = None
            self.head.next = node
            self.head = node

    def reset(self):
        self.head = self.root


class Stack:
    def __init__(self):
        self.container = LinkedList()

    def pop(self):
        def traverse(cont, node):
            cnode = cont.root
            while cnode.next is not None and cnode.next != node:
                cnode = cnode.next
            if cnode.next == node:
                return cnode
            return None

        res = traverse(self.container, self.container.head)
        if res is not None:
            to_return =  Node(self.container.head.value)
            self.container.head = res
            self.container.head.next = None
            return to_return

    def peek(self):
        return self.container.head

    def push(self, val):
        self.container.add(Node(val))



# --------- testing ---------

s = Stack()
s.push(1)
s.push(4)
s.push(8)


print("Should be true: ", s.peek().value == 8)
s.pop()
print("Should be true: ", s.peek().value == 4)






