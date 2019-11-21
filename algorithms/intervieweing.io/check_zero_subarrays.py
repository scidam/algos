#
#Check if zero subarray exists or not

arr = [4, 2, 1, 0]


# arr = [x1, x2, ... xn]
# Sj = x1+... + xj  complexity => O(n), space complexity O(n)
# Sj == Si j!=i => return True
# otherwise return False
# S(n+k) - S(n) == 0

# is duplicates in an array

def check_zero_subarray(arr):
    sk = [arr[0]]
    s = set(sk)
    for el in arr[1:]:
        sk.append(sk[-1] + el)
        if sk[-1] in s:
            return True
        else:
            s = s.union({sk[-1]})
    return False


print(check_zero_subarray(arr))
