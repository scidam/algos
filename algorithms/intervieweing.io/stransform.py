
start = 'dog'
end = 'hat'

voc = ['dot', 'cat', 'hot', 'hog', 'eat', 'dug', 'dig']


class Node:
    def __init__(self, word):
        self.word = word
        self.children = list()
        self.visited = False

    def __str__(self):
        return self.value

    __repr__ = __str__

dog_node = Node(start)

voc.append(end)

def diffs(s1, s2):
    return len(set(s1) - set(s2))


# build the graph

def recursive_builder(cnode, voc):
    if voc:
        to_del = []
        for v in voc:
            if diffs(v, cnode.value) <= 1:
                print("I am here", cnode)
                cnode.children.append(Node(v))
                to_del.append(v)
        voc = [el for el in voc if el not in to_del]
        for c in cnode.children:
            recursive_builder(c, voc)
    print("quitting")


def traverse(cnode):
    found = False
    def _traverse(cnode, path=[]):
        nonlocal found
        if not found:
            path.append(cnode)
            if cnode.value == end:
                found = True
                return path
            else:
                if cnode.children:
                    for child in cnode.children:
                        res = _traverse(child, path=path[:])
                        if found:
                            return res
        else:
            return path
    return _traverse(cnode)
    
#  -------- Another option is to use Breadth-first search algorithm ----

from queue import Queue


class Node:
    def __init__(self, word):
        self.word = word
        self.children = list()
        self.visited = False

    def __str__(self):
        return self.value
    
    def add_link(self, other):
        self.children.append(other)


class Graph:
    def __init__(self):
        self.words = {}

    @staticmethod
    def diff_eq1(w1, w2):
        """ Check if words differ no more than 1 letter """
        if not w1:
            return False
        if not w2:
            return False
        diff = 0
        for x, y in zip(w1, w2):
            if x != y:
                diff += 1
            if diff > 1:
                return False
        return True


    def add_word(self, word):
        if word not in self.words:
            self.words[word] = Node(word)


    def traverse_bsf(self, start, end):
        q = Queue()
        q.put(self.words[start])
        while not q.empty():
            cnode = q.get()
            cnode.visited = True
            if cnode == self.words[end]:
                return True
            for n in cnode.children:
                if not n.visited:
                    q.put(n)
        return False


    def is_transformable(self, start, end, dictionary):
        for w in dictionary:
            self.add_word(w)
        self.add_word(start)
        self.add_word(end)
        for w1 in self.words.keys():
            for w2 in self.words.keys():
                if self.diff_eq1(w1, w2):
                    self.words[w1].add_link(self.words[w2])
        return self.traverse_bsf(start, end)

g = Graph()
print(g.is_transformable('dog', 'hat', voc))
