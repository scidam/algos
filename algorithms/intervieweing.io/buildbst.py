# Build Balanced Binary Search Tree


class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

def build_tree(arr, root):
    n = len(arr)
    if n == 0:
        return
    middle = arr[n//2]
    root.value = middle
    left = arr[:n//2]
    right = arr[n//2+1:]
    root.left = Node()
    build_tree(left, root.left)
    root.right = Node()
    build_tree(right, root.right)

root = Node()
build_tree(range(10), root)

def print_tree(root, k=2):
    if root.value is not None:
        print('-' * k + "node: %s" % root.value)
        print_tree(root.left, k=k+2)
        print_tree(root.right, k=k+2)
    
print_tree(root)    
