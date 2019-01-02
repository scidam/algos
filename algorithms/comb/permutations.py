__author__ = "Dmitry E. Kislov"
__created__ = "02.01.2019"
__email__ = "kislov@easydan.com"


def get_permutations(array):
    """Returns all permutations for a given array

    **Parameters**

        :param array: an array like object, e.g. list
        :rtype: list
        :returns result: an array of all combinations formed from the input
                         array

    **Notes**

        It is not recommended to use with big arrays due to recursive
        structure of the algorithm implemented.
    """
    result = list()

    def permute(x, index, acc=[0] * len(array)):
        if index == len(array):
            result.append(acc[:])
            acc = list()
            return None
        for j in range(len(x)):
            acc[index] = x[j]
            _x = x[:]
            _x.pop(j)
            permute(_x, index + 1, acc)

    permute(array, 0)
    return result


if __name__ == '__main__':
    result = get_permutations(list(range(4)))
    print("The length of all permutations is: ", len(result))
    print("All permutations: ", result)
