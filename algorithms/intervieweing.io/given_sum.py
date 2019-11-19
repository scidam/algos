
# Find pair with given sum in array
#
arr = [1,3,5,8,19]
s = 11

def find_pair(arr, s):
    dct = dict()
    for item in arr:
        dct.update({s-item: item})

    for el in arr:
        val = dct.get(el, None)
        if val:
            return el, val
    return None


print("Pair is ", find_pair(arr, s))
