# find maximum product of two integers in array
#


arr = [-1, 4, 9, -10, -8]

def max_prod(arr):
    """ Find maximum product of 2 ints """

    fmax = smax = fmin = smin = arr[0]
    for k in range(len(arr)):
        if arr[k] > fmax:
            fmax = arr[k]
        if arr[k] < fmin:
            fmin = arr[k]

    for k in range(len(arr)):
        if arr[k] > smax and arr[k] != fmax:
            smax = arr[k]
        if arr[k] < smin and arr[k] != fmin:
            smin = arr[k]

    return max(fmin * smin, fmax * smax)

print("Expected value is 80: ", max_prod(arr))


