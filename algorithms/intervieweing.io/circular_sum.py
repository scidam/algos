
# Find maximum value in circular array

arr = [ 2, 1, -5, 4, -3, 1, -3, 4, -1]


def find_max(arr):
    mins = arr[0]
    maxs = arr[0]
    s = arr[0]
    for k in range(1, len(arr)):
        s = s + arr[k]
        mins = min(mins, s)
        maxs = max(maxs, s)

    minmax_non_circular = maxs - mins

    maxr = arr[-1]
    maxl = arr[0]
    sr = 0
    k = len(arr) - 1
    sl = 0
    j = 0
    while k > j:
        sr = sr + arr[k]
        sl = sl + arr[j]
        j += 1
        k -= 1
        maxr = max(sr, maxr)
        maxl = max(sl, maxl)

    return max(maxs - mins, maxr + maxl)


print(find_max(arr))
