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


def merge_sort(thelist, result=[], order='asc'):
    '''Sorting arrays by merging.

    **Parameters**

        :param thelist: an iterable to be sorted (tested with lists)
        :param result: an array for result storing
        :param order: a string, ordering option, default is 'asc'
        :returns: sorted list of input values
        :rtype: list

    '''
    n = len(thelist)
    if n == 1:
        left = [thelist[0]]
        right = []
        return left, right
    else:
        left = thelist[:n//2]
        right = thelist[n//2:]
    l, r = merge_sort(left, result=[], order=order)
    combined_l = combine(l, r)
    l, r = merge_sort(right, result=[], order=order)
    combined_r = combine(l, r)
    result.extend(combine(combined_l, combined_r))
    if order != 'asc':
        result = result[::-1]
    return combined_l, combined_r


if __name__ == '__main__':
    array_reversed = list(range(10)[::-1])
    print("Array to be sorted: ", array_reversed)
    result = []
    merge_sort(array_reversed, result=result)
    print('Result is ', result)
    simple_array = list(range(10))
    result = []
    merge_sort(simple_array, result=result)
    print('Result is ', result)
