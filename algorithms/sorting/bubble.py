__author__ = "Dmitry E. Kislov"
__created__ = "29.06.2018"
__email__ = "kislov@easydan.com"


def bubble_sort(array, order='asc'):
    """Bubble sorting algorithm.

    This is a bit smart implementation of the bubble sorting algoritm.
    It stops if obtained sequence is already ordered.

    **Parameters**

        :param array: an iterable to be sorted
        :param order: a string, defines ordering,  default value is `asc`
                     (that is ascending order)
        :type array: list, tuple
        :type order: string
        :returns: sorted list of input values
        :rtype: list

    """

    from operator import lt, gt
    n = len(array)
    sorted_array = list(array)
    comparison = lt if order == 'desc' else gt
    for j in range(n):
        done = True
        for i in range(n - j - 1):
            if comparison(sorted_array[i], sorted_array[i + 1]):
                sorted_array[i + 1], sorted_array[i] = \
                    sorted_array[i], sorted_array[i + 1]
                done = False
        if done:
            break

    return sorted_array


if __name__ == '__main__':
    array = range(10)
    print("Source array: {}".format(array))
    sorted_array = bubble_sort(array)
    print("Sorted array: {}".format(sorted_array))

    array_reversed = range(10)[::-1]
    print("Reversed array: {}".format(array_reversed))
    sorted_array = bubble_sort(array_reversed)
    print("Sorted array: {}".format(sorted_array))
