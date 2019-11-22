
# Build alien dictinary based on 
# a given order of words

#bgg
#fbg
#fqf
#ffq
#gfg


class Node:
    def __init__(self, c):
        self.c = c
        self.next = None

class G:
    def __init__(self):
        self.graph = list()

    def add_node(self, c1, c2):
        if (c1, c2) not in self.graph:
            self.graph.append(c1, c2)

    def outgoing(self, c):
        return [y for x, y in self.graph if x == c]

    def incoming(self, c):
        return [x for x, y in self.graph if y == c]
