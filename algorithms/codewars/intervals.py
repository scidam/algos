from operator import itemgetter

def is_intersected(i, j):
    a, b = min(i), max(i)
    c, d = min(j), max(j)
    if a<=c and b >= c and d >= b:
        return True
    elif a<=c and b >= c and d <= b:
        return True
    elif a >= c and a <= d and b>=d:
        return True
    elif a >=c and a <= d and b <=d:
        return True
    return False

def merge(i, j):
    a, b = min(i), max(i)
    c, d = min(j), max(j)
    if a<=c and b >= c and d >= b:
        return [a, d]
    elif a<=c and b >= c and d <= b:
        return [a, b]
    elif a >= c and a <= d and b>=d:
        return [c, b]
    elif a >=c and a <= d and b <=d:
        return [c, d]
    return None



def compute_sum(s):
    ss = sorted(s, key=itemgetter(0, 1), reverse=True)
    res = [ss.pop()]
    while ss:
        print(res)
        el = ss.pop()
        if is_intersected(el, res[-1]):
            rr = merge(el, res[-1])
            res.pop()
            res.append(rr)
        else:
            res.append(el)

    return sum(map(lambda x: abs(x[0] - x[1]), res))



print(compute_sum([[-100,200], [-10, 11], [-1000,-500]]))

# def compute_sum(s):
#     def merge_intervals(invals,  new):
#         for k in range(len(invals)):
#             if is_intersected(invals[k], new):
#                 nn = merge(invals[k], new)
#                 invals = merge_intervals(invals[:k-1] + invals[k+1:], nn)
#         else:
#             for item in invals:
#                 if is_intersected(item, new):
#                     return invals
#             else:
#                 invals.append(new)
#                 return invals
#     ll = s[:]
#     res = list()
#     res.append(ll.pop())
#     while ll:
#         el = ll.pop()
#         res = merge_intervals(res, el)
#     return sum(map(lambda x: abs(x[0] - x[1]), res))



