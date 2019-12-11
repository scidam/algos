# implementation of the min heap (i.e. priority-queue)
arr = [5, 1, 2, 7, 18, 0, 4, 2, 6]

""" Example:
[5, 1, 6, 18, 12, 3]

           5 
        /     \
      1        6
    /   \     /  \
  18     12  3    None    // h = [log2(n)] + 1

k-th node at 2*k
k-th node child left 2*k+1
k-th node child right 2*k + 2
[(k-1)/2] -- parent of the k-th node
"""

def less(a, b):
    return a < b

def greater(a, b):
    return a > b

def heapify(arr, n, root, op=less):
    maxind = root
    left = 2 * root + 1
    right  = 2 * root + 2
    if left < n and op(arr[left], arr[maxind]):
        maxind = left

    if right < n and op(arr[right], arr[maxind]):
        maxind = right        

    if maxind != root:
        arr[root], arr[maxind] = arr[maxind], arr[root]
        heapify(arr, n, maxind, op=op)


def build_heap(arr, op=less):
    n = len(arr)
    for i in range(int(n/2)-1, -1, -1):
        heapify(arr, n, i, op=op)

print("Before: ", arr)
build_heap(arr)
print("After: ", arr)
