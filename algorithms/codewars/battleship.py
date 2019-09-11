from itertools import groupby, product


def check_diag(f, i, j):
    n = len(f)

    if i > 0 and i < n-1:
        deltai = [1, -1]
    elif i == n-1:
        deltai = [-1]
    elif i == 0:
        deltai = [1]

    if j > 0 and j < n-1:
        deltaj = [1, -1]
    elif j == n-1:
        deltaj = [-1]
    elif j == 0:
        deltaj = [1]

    return (f[i][j] and  not any([f[di+i][dj+j] for di, dj in product(deltai, deltaj) if abs(di) == abs(dj)])) or not f[i][j]
    


def check_one_cell(f, i, j):
    n = len(f)

    if i > 0 and i < n-1:
        deltai = [1, -1, 0]
    elif i == n-1:
        deltai = [-1, 0]
    elif i == 0:
        deltai = [1, 0]

    if j > 0 and j < n-1:
        deltaj = [1, -1, 0]
    elif j == n-1:
        deltaj = [-1, 0]
    elif j == 0:
        deltaj = [1, 0]

    return f[i][j] and not any([f[di+i][dj+j] for di, dj in product(deltai, deltaj) if abs(di)!=abs(dj)])

def validate_battlefield(f):
    n = len(f)
    allowed = {4:1, 3:2, 2:3, 1:4}
    real = {4:0, 3:0, 2:0, 1:0}
    
    for row in f:
        s = 0
        for val, gr in groupby(row):
            s = sum(gr)
            if s > 1:
                try:
                    real[s] += 1
                except:
                    return False

    for col in zip(*f):
        s = 0
        for val, gr in groupby(col):
            s = sum(gr)
            if s > 1:
                try:
                    real[s] += 1 
                except:
                    return False
    for i in range(n):
        for j in range(n):
            if check_one_cell(f, i, j):
                real[1] += 1
            if not check_diag(f, i, j):
                return False
    
    for k in allowed.keys():
        if real[k]!=allowed[k]:
            return False
    return True
    
    
   
battleField = [[0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
[1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 1, 1]
]



print(validate_battlefield(battleField))
