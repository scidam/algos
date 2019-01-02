__author__ = "Dmitry E. Kislov"
__created__ = "29.12.2018"
__email__ = "kislov@easydan.com"


def binary_search(x, array):
    '''Binary search algorithm. Recursive implementation.

    **Parameters**

       :param x: an object, the element that should be found
       :param array: sorted array of objects
       :returns: the found object; if the object doesn't belong to the array
                 returns None
       :rtype: the same type as x or None

    '''
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


if __name__ == "__main__":
    data = sorted([1, 3, 5, 3, 2, 1, 5, 6, 7, 8, 4, 3, 2, 1, 5])
    print("Result is ", binary_search(6, data))
