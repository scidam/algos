__author__ = "Dmitry E. Kislov"
__created__ = "10.01.2019"
__email__ = "kislov@easydan.com"

import numpy as np


class Node:
    """Base node class.

    Instances of this class represents nodes of an abstract tree.

    **Parameters**

        :param value: float or integer, the node's value
        :param parent: instance of Node class, parent node or None (for root nodes)
    """

    def __init__(self, value, parent=None):
        self.parent = parent
        self.value = value

    def __repr__(self):
        if self.parent is None:
            return "Root node: %s" % self.value
        else:
            return "Node: %s (Parent node is %s)" % (self.value, self.parent.value)

    def __str__(self):
        thestring = ''
        thestring += "=" * 10 + '\n'
        thestring += "Node value is %s \n" % self.value
        if self.parent is not None:
            thestring += "Parent node: %s\n" % self.parent.value
        else:
            thestring += "This is root node!\n"
        thestring += "=" * 10 + "\n"
        return thestring


class HeapMax:

    def __init__(self, objects):
        self.source = objects
        self.root = None
        self.unordered_nodes = set()

    def build_binary_max_heap(self):
        objs = sorted(self.source)
        self.root = Node(objs.pop())
        self.unordered_nodes.update({self.root})
        leaf_nodes = list()
        leaf_nodes.append(self.root)
        while objs:
            o1 = objs.pop()
            o2 = objs.pop()
            n1 = None
            print(leaf_nodes)
            for item in leaf_nodes:
                if item.value >= o1 and item.value >= o2:
                    n1 = Node(o1, parent=item)
                    n2 = Node(o2, parent=item)
                    self.unordered_nodes.update({n1})
                    self.unordered_nodes.update({n2})
                    break
            if n1 is not None:
                leaf_nodes.remove(item)
                leaf_nodes.append(n1)
                leaf_nodes.append(n2)

    def print(self):
        print("Unordered set of nodes: ", self.unordered_nodes)


if __name__ == '__main__':
    objs = np.random.randint(1, 100, size=7).tolist()
    heap = HeapMax(objs)
    heap.build_binary_max_heap()
    heap.print()
