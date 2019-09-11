import re
from itertools import groupby
from operator import itemgetter, neg, add

xyz_pat = re.compile('[a-z]+')
d_pat = re.compile('\d+')
poly_pat =re.compile(r'(\s?[\-\+]?\s?)([a-z0-9]+)')

def minimize(s):
    def decomp(c):
        digs = d_pat.findall(c) or [1]
        w = xyz_pat.findall(c) or ['']
        return int(digs[0]), ''.join(sorted(w[0]))

    s = s.lower().strip()
    components = poly_pat.findall(s)
    decomposed = [(s, ) + tuple(decomp(v)) for s, v in components]

    simplified  = list()
    for g, c in groupby(sorted(decomposed, key=itemgetter(-1)), key=itemgetter(-1)):
        s = 0
        for item in c:
            if item[0] == '+':
                s = add(s, item[1])
            elif item[0] == '-':
                s = add(s, neg(item[1]))
            else:
                s = add(s, item[1])
        if s != 0:
           simplified.append((g, s))

    sorted_poly = sorted(simplified, key=lambda x: (len(x[0]), x[0]))
    final = ''
    for i, item in enumerate(sorted_poly):
        if abs(item[1]) == 1:
            val = ''
        else:
            val = str(abs(item[1]))
        if i == 0:
            final += ('-' if item[1] < 0 else '') + val + item[0]
        else:
            final += ('+' if item[1] > 0 else '-') + val + item[0]
    return final

print(minimize("-a+5ab+3a-c-2a"))
    
                
        
           
    
    
    
    
