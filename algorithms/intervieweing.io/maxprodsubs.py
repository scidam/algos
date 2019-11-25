# Maximum Product Subset Problem


def max_prod(arr):
    _arr = [el for el in arr if el != 0]
    minel = None
    num_neg = 0
    for el in _arr:
        if el < 0:
            if minel is None:
                minel = el
            else:
                minel = max(minel, el)
            num_neg += 1
    res = 1
    if num_neg > 0 and num_neg % 2 == 0:
        for el in _arr:
            res *= el
        return res
    elif num_neg > 0 and num_neg % 2 > 0:
        cc = 0
        for el in _arr:
            if el != minel or (el == minel and cc > 0):
                res *= el
            if el == minel:
                cc += 1
        return res
    else:
        for el in _arr:
            res *= el
        return res



arr = [-6, 4, -5, 8, -10, 0, 8]


print(max_prod(arr))

                

    

