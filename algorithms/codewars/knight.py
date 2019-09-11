from itertools import product

def all_variants(i, j):
    return [(di+i, dj+j) for di, dj in [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)] if 0<=di+i<8 and 0<=dj+j<8]

def shortest(a, b):
    mapper = {k:v for k,v in zip('abcdefgh', range(8))}
    marked = dict()
    a = (mapper.get(a[0]), int(a[1])-1)
    b = (mapper.get(b[0]), int(b[1])-1)
    
    l=1
    vars = all_variants(*a)
    for v in vars:
        marked[v] = 1
        if v == b:
            return l
    while True:
        for k in list(marked.keys()):
            vars = all_variants(*k)
            for v in vars:
                if v == b:
                    return marked[k] + 1
                elif v not in marked:
                    marked[v] = marked[k] + 1
                    

print(shortest('a3', 'b5'))
