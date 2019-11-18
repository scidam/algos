
class Node:
    def __init__(self, match, s='', name=''):
        self.children = list()
        self._match = match
        self.name = name
        self.s = s

    def match(self, x):
        return self._match(x, self.s)

    def __str__(self):
        return self.name


def match_symbol(x, s):
    return x == s if s != '.' else True

def match_any_az(x, s=''):
    return x in 'abcdefghijklmnopqrstvuwxyz'


def build_graph(p):
    rootNode = Node(lambda x: True, name='Root Node')
    lastNode = rootNode
    k = 0
    while k < len(p):
  #      print("Current symbol: ", p[k])
        if p[k] in 'abcdefghijklmnopqrstvuwxyz.':
            if  k<len(p)-1 and p[k + 1] == '*':
                cnode = Node(match_symbol, s=p[k], name='Matching, kleenstar: {}'.format(p[k]))
                cnode.children.append(cnode)
                lastNode.children.append(cnode)
                k += 2
                continue
            elif k<len(p) - 1 and p[k+1] not in '*[':
                cnode = Node(match_symbol, s=p[k], name='Matching: {}'.format(p[k]))
                lastNode.children.append(cnode)
                k += 1
                lastNode = cnode
                continue
            else:
  #              print("Value, ", p[k])
                cnode = Node(match_symbol, s=p[k], name='Matching: {}'.format(p[k]))
                lastNode.children.append(cnode)
                lastNode = cnode
                k += 1
                continue

        if p[k:k+5] =='[a-z]':
            if p[k+6:].startswith('*'):
                cnode = Node(match_any_az, s='', name='Matching a-z')
                cnode.children.append(cnode)
                lastNode.children.append(cnode)
                k += 5
            elif not p[k+6:].startswith('*'):
                cnode = Node(match_any_az, s='', name='Rgular node az')
                lastNode.children.append(cnode)
                lastNode = cnode
                k += 5
            else:
                k+=5
    return rootNode

nn = build_graph('ab[a-z]c.*d')



visited = list()

def pprint_nodes(node, k=2):
    if node.children and id(node) not in visited:
        print('-' * k, node, id(node))
        visited.append(id(node))
        for n in node.children:
            pprint_nodes(n, k=k+2)
    else:
        if node not in visited:
            visited.append(id(node))
            print('-' * k, node, id(node))



def match(s, p):
    """ Allowed patterns:
        p = [a-z] -- specific symbol (lower case only)
        p = '*' -- Kleene star
        p = '.' -- any symbol
    """
    root = build_graph(p)
    cnode = root
    for k in range(len(s)):
        for n in cnode.children:
            print(n)
            if n.match(s[k]):
                cnode = n
                break
        else:
            if k < len(s):
                return False
    if cnode.children:
        if id(cnode.children[0]) != id(cnode):
            return False
    return True


g = build_graph('a')

print("Trying two strings: ", match('abcddccd', 'ab.*'))
