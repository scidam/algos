__author__ = "Dmitry E. Kislov"
__created__ = "02.01.2019"
__email__ = "kislov@easydan.com"


def insertion_sort(array):
    """Sort array by the insertion sort algorithm.

    **Algorithm**
        Given an array X = [x1, ..., xN] the insertion sort
        algorithm starts at position `pos` and performs
        insertion of the X[pos] into appropriate position
        of the subarray X[0:pos-1].

    **Complexity**
        :math:`O(n^2)`

    **Note**
        This algorithm changes the input array.
        In this implementation of sorting algorithm allowsls sort in
        ascending order only.
    """

    for pos in range(1, len(array)):
        for i in range(pos):
            if array[pos] < array[i]:
                array.insert(i, array.pop(pos))
                break
    return array


if __name__ == '__main__':
    array_reversed = [1, 4, 7, 3, 5, 2, 4, 4, 10, 9, 11]
    print("Array to be sorted: ", array_reversed)
    print('Result is ', insertion_sort(array_reversed))
