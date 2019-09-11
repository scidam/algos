
def helper(m, n):
    prep = list(range(m + (n - divmod(m ,n)[1] if m%n != 0 else 0)))
    res = list()
    for i in range(n):
        ind = i
        k = 1
        res.append(prep[ind])
        while True:
            if k % 2:
                incr = 2 * (n - i - 1)
            else:
                incr = 2 * i 
            if incr > 0:
                ind += incr
                if ind < len(prep):
                    res.append(prep[ind])
                else:
                    break
            k += 1
    return res



def encode_rail_fence_cipher(string, n):
    m = len(string)
    if m == 0: return ''
    return ''.join(string[i] for i in helper(m, n) if i < m)
    
def decode_rail_fence_cipher(string, n):
    m = len(string)
    if m == 0: return ''
    t = m + (n - divmod(m ,n)[1] if m%n != 0 else 0)
    f = list(filter(lambda x: x<m, helper(t, n)))
    ss = sorted([(a, b) for a, b in zip(f, range(len(f)))], key=lambda x:x[0])
    return ''.join(string[k] for k in [s[1] for s in ss])
                
print(decode_rail_fence_cipher(encode_rail_fence_cipher("I am dmitry! heroes", 3), 3))
