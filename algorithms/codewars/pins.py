
def cartesian(*args):
    if not args:
        return [[]]
    else:
        
        res = cartesian(*args[1:])
        newres = list()
        for item in args[0]:
            for p in res:
                newres.append(p[:]+ [item])
        return newres

from itertools import product        
        

def get_pins(s):
    neighbors = {'1': ['1', '2', '4'],
                 '2': ['2', '1', '5', '3'],
                 '3': ['3', '2', '6'],
                 '4': ['4', '1', '5', '7'],
                 '5': ['5', '2', '4', '6', '8'],
                 '6': ['6', '5', '3', '9'],
                 '7': ['4', '8', '7'],
                 '8': ['8', '5', '7', '9', '0'],
                 '9': ['9', '8', '6'],
                 '0': ['0', '8']
                 }
    seq = [neighbors.get(l) for l in s]
    return list(map(''.join, product(*seq)))

    
    

   
            
