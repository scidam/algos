
def sums(n):
    squares = [k**2 for k in range(2, n+1) if k*k < 2 * n - 1]
    print(squares)
    done = False
    arange = list(range(1, n+1))
    sample = [arange.pop()]
    while not done:
        if len(sample) == n:
            return sample
        print(sample)
        for item in arange[::-1]:
           if (item + sample[0]) in squares:
                sample = [item] + sample
                arange.remove(item)
                break
           if (item + sample[-1]) in squares:
                sample.append(item)
                arange.remove(item)
                break
        else:
            return False


def check_sums(N):
    squares = [k ** 2 for k in range(2, N + 1) if k * k <= 2 * N - 1]

    # precomputing allowed values
    precomp = dict()
    for k in range(1, N + 1):
        precomp[k] = list()
        for s in squares:
            if N >= s - k > 0:
                precomp[k].append(s - k)
        precomp[k] = list(set(precomp[k]))
    done = False
    sample = [N]
    candidates = list()
    candidates.append([('left', value) for value in precomp[sample[0]]])
    candidates[-1].extend([('right', value) for value in precomp[sample[0]]])
    history = list()
    history.append(sample[:])
    last_appended = None
    while candidates:
        #print("=" * 10)
        #print("=" * 10)
        cval = None
        if candidates[-1]:
            cval = candidates[-1].pop()
            if cval[0] == 'left':
                sample = [cval[1]] + sample
            elif cval[0] == 'right':
                sample.append(cval[1])
            last_appended = cval
            
            if len(sample) == N:
                return sample

            vals0 = [value for value in precomp[sample[0]] if value not in sample]
            vals1 = [value for value in precomp[sample[-1]] if value not in sample]
            
            if vals0 + vals1:
                candidates.append([])
                history.append(sample[:])
                if vals0:
                    candidates[-1].extend([('left', value) for value in vals0])
                if vals1:
                    candidates[-1].extend([('right', value) for value in vals1])
            else:
                sample = history[-1][:]

        else:
            candidates.pop()
            if not candidates:
                break
            history.pop()
            sample = history[-1][:]
            
    return False



def check_sums1(N):
    squares = [k ** 2 for k in range(2, N + 1) if k * k <= 2 * N - 1]

    # precomputing allowed values
    precomp = dict()
    for k in range(1, N + 1):
        precomp[k] = list()
        for s in squares:
            if N >= s - k > 0:
                precomp[k].append(s - k)
        precomp[k] = sorted(list(set(precomp[k])), reverse=True)
    done = False
    sample = [N]
    candidates = list()
    candidates.append([('left', value) for value in precomp[sample[0]]])
    history = list()
    history.append(sample[0])
    last_appended = None
    while candidates:
        #print("=" * 10)
        #print("HIstory length: ", len(history))
        #print("=" * 10)
        if candidates[-1]:
            cval = candidates[-1].pop()
            if cval[0] == 'left':
                sample = [cval[1]] + sample
            elif cval[0] == 'right':
                sample.append(cval[1])
            last_appended = cval[1]

            if last_appended:
                history.append(last_appended)
            
            if len(sample) == N:
                return sample

            vals0 = [value for value in precomp[sample[0]] if value not in sample]
            vals1 = [value for value in precomp[sample[-1]] if value not in sample]

            if vals0 + vals1:
                candidates.append([])
                if vals0:
                    candidates[-1].extend([('left', value) for value in vals0])
                if vals1:
                    candidates[-1].extend([('right', value) for value in vals1])
            else:
                sample.remove(history.pop())
        else:
            candidates.pop()
            if not candidates:
                break
            sample.remove(history.pop())
            
            
    return False
 
 
 
def square_sums_row(n):

    def dfs():
        print(inp, res)
        if not inp:
            yield res
        for v in tuple(inp):
            print("v=", v)
            if not res or not ((res[-1]+v)**.5 % 1):
                print("Adding value:", v)
                res.append(v)
                inp.discard(v)
                yield from dfs()
                print("popping", res[-1])
                inp.add(res.pop())
            else:
                print("omiting value: ", v)

    inp, res = set(range(1,n+1)), []
    return next(dfs(), False) 
 
print(square_sums_row(5))

#for j in range(5, 30):
#    print("j= %s | %s"%(j, check_sums1(j)))
