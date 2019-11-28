# Find subarray of a given size and having minimum sum of elements

arr = [1,4,2,6,7,3,1,2,2,3]
size = 3

def find_min(arr, size=size):
    ss = sum(arr[:size])
    i = 0
    j = size - 1
    mem = (i, j)
    while j < len(arr) - 1:
        j += 1 
        i += 1
        probe = ss - arr[i - 1] + arr[j]
        print(ss, probe, i, j, arr[i - 1], arr[j])
        if probe < ss:
            mem = (i, j)
    return (*mem, sum(arr[mem[0]:mem[1] + 1]))

print(find_min(arr))
