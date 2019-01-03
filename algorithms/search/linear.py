__author__ = "Dmitry E. Kislov"
__created__ = "02.01.2019"
__email__ = "kislov@easydan.com"


def linear_search(x, array):
    '''Linear search algorithm

    **Parameters**

       :param x: an object, the element to be found
       :param array: an array like object, e.g. list
       :returns: index of the element found or -1 if the element was not found
       :rtype: int

    **Complexity**
        :math:`O(n)`

    **Note**
        Use zero-indexing notation when do searching the elemnt.
    '''
    for ind, el in enumerate(array):
        if el == x:
            return ind
    else:
        return -1


if __name__ == "__main__":
    data = [1, 3, 5, 3, 2, 1, 5, 6, 7, 8, 4, 3, 2, 1, 5]
    print("Result is ", linear_search(5, data))
