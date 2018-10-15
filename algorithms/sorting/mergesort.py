__author__ = "Dmitry E. Kislov"
__created__ = "15.10.2018"
__email__ = "kislov@easydan.com"

def combine(left, right):
    combined = []
    n, m = len(left), len(right)
    if n * m == 0:
        combined.extend(left)
        combined.extend(right)
        return combined
    for j in range(min(n, m)):
        print(left, right)
        if left[j] <= right[j]:
            combined.append(left[j])
            combined.append(right[j])
        else:
            combined.append(right[j])
            combined.append(left[j])
    if n >= m:
        combined.extend(left[n - m + 2:])
    else:
        combined.extend(right[m - n + 2:])
    return combined


def test_combine():
    print('Testing combine function ... ')
    result1 = combine([1,5,12,90], [-2, 4, 20, 110, 160, 500])
    result2 = combine([-2, 4, 20, 110, 160, 500], [1, 5, 12, 90])
    if result1 == result2:
        print("Test for the combine function is passed!")
    else:
        print("Something is wrong with the combine function!")


def merge_sort(thelist, sorted=[]):
    '''
    Sorting by array merging.
    NOT COMPLETED YET!!!!

    '''
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
    print('Left = ', left, 'Right = ', right)
    l, r = merge_sort(left, sorted=sorted)
    combined_l = combine(l, r)
    print('1) L = ', l, 'R = ', r)
    print("1) Combined :", combined_l)
    l, r = merge_sort(right, sorted=sorted)
    combined_r = combine(l, r)
    print('final L = ', l, 'R = ', r)
    print("final combined ", combined_r)
    return left, right


if __name__ == '__main__':
    array_reversed = list(range(10)[::-1])
    sorted = merge_sort(array_reversed)
