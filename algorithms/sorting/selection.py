__author__ = "Dmitry E. Kislov"
__created__ = "02.01.2019"
__email__ = "kislov@easydan.com"


def selection_sort(array, order='asc'):
    """Recursive implementation of the selection sort algorithm

    **Parameters**

        :param array: an array like object, e.g. list
        :returns: array of sorted elements
        :param order: a string, ordering option, default is 'asc'
        :rtype: list

    **Algorithm**
        The selection sort algorithm sorts an array by repeatedly
        finding the minimum or maximum element
        from unsorted part and putting it at the beginning

    **Complexity**
        :math:`O(n^2)`

    **Note**
        This is recursive implementation of the algorithm.
        Be careful of using it with arrays of big size.

    **Links**
        https://www.geeksforgeeks.org/selection-sort/
    """

    def get_minimum(x):
        if len(x) == 1:
            return (x[0], 0)
        elif len(x) == 0:
            return None
        min_value = x[0]
        res = None
        for j, el in enumerate(x[1:]):
            if el < min_value:
                res = (el, j + 1)
                min_value = el
        return res or (min_value, 0)

    def algorithm(x, sorted):
        min_tuple = get_minimum(x)
        if min_tuple is not None:
            sorted.append(min_tuple[0])
        elif min_tuple is None:
            return sorted
        _x = x[:]
        _x.pop(min_tuple[-1])
        algorithm(_x, sorted)
        return sorted

    if order == 'asc':
        return algorithm(array, list())
    else:
        _array = [-el for el in array]
        return [-el for el in algorithm(_array, list())]


def selection_sort_nonrecursive(array, order='asc'):
    """Non-recursive implementation of the selection sort algorithm
    """

    def sort_it(array):
        for i in range(len(array)):
            min_index = i
            for j in range(i+1, len(array)):
                if array[min_index] > array[j]:
                    min_index = j
            array[i], array[min_index] = array[min_index], array[i]
        return array

    if order == 'asc':
        return sort_it(array)
    else:
        _array = [-el for el in array]
        return [-el for el in sort_it(_array)]


if __name__ == '__main__':
    array_reversed = list(range(10)[::-1])
    print("Array to be sorted: ", array_reversed)
    print('Result is ', selection_sort(array_reversed))
    simple_array = list(range(10))
    print("Array to be sorted: ", simple_array)
    print('Result is ', selection_sort(simple_array, order='desc'))

    print("Using non-recursive implementatino of the algorithm: ")
    print('Result is ', selection_sort_nonrecursive(simple_array, order='desc'))
    print('Result is ', selection_sort_nonrecursive(array_reversed, order='asc'))
