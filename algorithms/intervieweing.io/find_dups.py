arr = [1,2,3,4,5,5]

reduce = lambda x, y: x ^ y

# a ^ b ^ c  = a ^ c ^ b


def find_dup(arr):
    el = arr[0]
    for k in range(1, len(arr)):
        el = reduce(el, arr[k])
        el = reduce(el, k)
    return el


print("Duplicated element is ", find_dup(arr))


