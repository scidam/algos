# -*- coding:utf-8 -*-
"""
Created Date: Thursday November 21st 2019
Author: Dmitry Kislov
E-mail: kislov@easydan.com
-----
Last Modified: Thursday, November 21st 2019, 5:35:35 pm
Modified By: Dmitry Kislov
-----
Copyright (c) 2019
"""

def quicksort(arr):
    """ Recursive implementation of quicksort algorithm """

    if len(arr) == 1 or len(arr) == 0:
        return arr
    if len(arr) == 2:
        return sorted(arr)

    pivot = arr[-1]
    left = quicksort([el for el in arr if el < pivot])
    right = quicksort([el for el in arr if el > pivot])

    right = [pivot] * arr.count(pivot) + right[:]

    # merge left and right parts

    if len(left) == 0 or len(right) == 0:
        return left + right

    if left and right and left[-1] <= right[0]:
        return left + right

    result = list()
    lind = 0
    rind = 0
    while lind != len(left) - 1 and  rind != len(right) - 1:
        l = left[lind]
        r = right[rind]
        if l <= r:
            result.append(l)
            lind += 1
        else:
            result.append(r)
            rind += 1
    if lind >= len(left) - 1:
        result += right[rind:]
    if rind >= len(right) - 1:
        result = left[lind:] + result
    return result


import random
arr = [random.randint(10, 100) for k in range(10)]
print("Unsorted array: ", arr)
ss = quicksort(arr)
print("Sorted array: ", ss)
