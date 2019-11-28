from math import log, exp

# Max product of positive numbers (using log and exponentiation)
# lets reduce the problem to finding max-sum

arr = [3, 4, 1, 5, 0]

def maxprod_subset(arr):
    _arr = list(filter(lambda x: x != 0 and x != 1, arr))
    print(_arr)
    _arr = list(map(log, _arr))
    _arr = list(filter(lambda x: x > 0, _arr))
    return exp(sum(_arr))

print(maxprod_subset(arr))  # Almost exact answer.