# Sort array where one element is swapped with another

def sort_swapped(arr):
    """ Sort almost sorted array """

    indi = None
    indj = None
    for k in range(len(arr) - 1):
        if arr[k] > arr[k+1]:
            if indi is None:
                indi = k
            elif indj is None:
                indj = k + 1
    arr[indi], arr[indj] = arr[indj], arr[indi]
    return arr

#arr = [3, 5, 6, 9, 8, 7]
arr =[3, 8, 6, 7, 5, 9]

print(arr)
print(sort_swapped(arr))