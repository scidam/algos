__author__ = "Dmitry E. Kislov"
__created__ = "15.10.2018"
__email__ = "kislov@easydan.com"


def combine(left, right):
    combined = []
    left = left[::-1]
    right = right[::-1]
    while bool(right) and bool(left):
        el1 = left.pop()
        el2 = right.pop()
        if el1 < el2:
            combined.append(el1)
            right.append(el2)
        else:
            combined.append(el2)
            left.append(el1)
    if left:
        combined.extend(left[::-1])
    elif right:
        combined.extend(right[::-1])
    return combined


def test_combine():
    print('Testing combine function ... ')
    x = [1, 5, 12, 90]
    y = [-2, -1, 0,  20, 21, 22, 110, 160, 500]
    print("Combining x, y", x, y)
    result1 = combine(x, y)
    print("Combining y, x", y, x)
    result2 = combine(y, x)
    print('Combining last example')
    z = combine([7], [5, 6])
    if result1 == result2 and z == [5, 6, 7]:
        print("Test for the combine function is passed!")
    else:
        print("Something is wrong with the combine function!")


def merge_sort(thelist, sorted=[]):
    '''
    Sorting by array merging.
    NOT COMPLETED YET!!!!

    '''
    print("Called mergesort")
    n = len(thelist)
    if n == 1:
        left = [thelist[0]]
        right = []
        return left, right
    elif n == 2:
        left = [thelist[0]]
        right = [thelist[1]]
        return left, right
    else:
        left = thelist[:n//2]
        right = thelist[n//2:]
    l, r = merge_sort(left, sorted=sorted)
    combined_l = combine(l, r)
    l, r = merge_sort(right, sorted=sorted)
    combined_r = combine(l, r)
    return combined_l, combined_r


if __name__ == '__main__':
    test_combine()
    array_reversed = list(range(10)[::-1])
    l1, l2 = merge_sort(array_reversed)
    result = combine(l1, l2)
    print('Result is ', result)
