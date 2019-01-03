__author__ = "Dmitry E. Kislov"
__created__ = "29.12.2018"
__email__ = "kislov@easydan.com"


def binary_search(x, array):
    """Binary search algorithm. Recursive implementation.

    **Parameters**

       :param x: an object, the element that should be found
       :param array: sorted array of objects
       :returns: the found object; if the object doesn't belong to the array
                 returns None
       :rtype: the same type as x or None

    **Complexity**

        :math:`O(log(n))`

    **Note**

        It is assumed that 0-indexing system is used

    """

    if len(array) == 0:
        return None
    if len(array) == 1:
        if x == array[0]:
            return array[0]
        else:
            return None
    if len(array) == 2:
        if x == array[0]:
            return array[0]
        elif x == array[1]:
            return array[1]
        else:
            return None
    if len(array) > 2:
        middle = len(array) // 2
        left = array[:middle]
        right = array[middle:]
        if x > left[-1]:
            res = binary_search(x, right)
        else:
            res = binary_search(x, left)
    return res


def binary_search_nonrecursive(x, array):
    """Non-recursive version of the binary search algorithm

    **Parameters**

        :param x: an object to be found
        :param array: an array like object where `x` object will be looked for
        :returns: an index of the object (if the elemnt was found) or -1
        :rtype: int

    """

    done = False
    _array = array[:]
    index = 0
    while not done:
        if len(_array) > 2:
            n = len(_array) // 2
            if x > _array[:n][-1]:
                index += n
                _array = _array[n:]
            else:
                _array = _array[:n]
        elif len(_array) == 2:
            done = True
            if x != _array[1] and x != _array[0]:
                index = -1
            elif x == _array[1]:
                index += 1
            elif x == _array[0]:
                index += 0
        elif len(_array) == 1:
            if x != _array[0]:
                index = -1
            done = True
        else:
            index = -1
            done = True

    return index


if __name__ == "__main__":
    data = sorted([1, 3, 5, 3, 2, 1, 5, 6, 7, 8, 4, 3, 2, 1, 5])
    print("Source dataset is ", data)
    print("Result is ", binary_search(30, data))
    print("Result is ", binary_search_nonrecursive(8, data))
