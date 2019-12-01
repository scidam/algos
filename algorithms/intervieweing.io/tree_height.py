# get tree height (e.g. binary tree)


def tree_height(tree):
    if tree is None:
        return 0
    if tree.left is None and tree.right is None:
        return 1
    height = 1 + max(tree_height(tree.left), tree_height(tree.right))
    return height



class Node:
    ...


root = Node()
rl1 = root.left = Node()
rr1 = root.right = Node()
rl1.left = None
rl1.right = None
rr1.left = None
rr1.right = Node()
rr1.right.left = None
rr1.right.right = None
print(tree_height(root))



