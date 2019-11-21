


# Find maximum subarray having given sum
# NOT YET SOLVED

arr = [5, 6, -5, 5, 3, 5, 3, -2, 0]

def max_len_subarray(arr, given_num=8):
    print("Source array: ", arr)
    if not arr:
        return False

    sk = [0]
    for el in arr:
        sk.append(sk[-1] + el)

    ss =dict()
    for i in range(len(sk)):
        ss.update({given_num + sk[i]: (sk[i], i)})

    for i in range(len(sk)):
        val = ss.get(sk[i], None)
        if val:
            print(val, i)
            if i >= val[-1]:
                return [val[-1], i-1]

    return None



print(max_len_subarray(arr))





