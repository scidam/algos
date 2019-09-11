

# This example solves more general problem 
def reducePath(arr):
    mapper = {
                'north': 1j,
                'south': -1j,
                'west': -1 + 0j,
                'east': 1 + 0j
              }
    paths = list(map(mapper.get, map(str.lower, arr)))
    res = list()
    for j in range(0, len(paths)):
        for k in range(j + 2,  len(paths) + 1):
            res.append((k - j, (j, k), sum(paths[j:k])))

    # reducing
    to_reduce = list()
    for item in sorted(filter(lambda x: x[-1]==0, res), key=lambda x: x[0], reverse=True):
        if not any(x<=item[1][0]<=y for x, y in to_reduce):
          to_reduce.append(item[1])
          
    result = [arr[j] for j in range(len(arr)) if j not in sum((list(range(i, j)) for i,j in to_reduce), [])]

    return result




# This example solves more general problem 
def reducePath(arr):
    _ = arr[:]
    def reducer(arr):
        res = arr[:]
        for j in range(0, len(arr)-1):
            if set([arr[j].lower(), arr[j+1].lower()])==set(['north', 'south']) or set([arr[j].lower(), arr[j+1].lower()])==set(['east', 'west']):
                sub = arr[:j] + arr[j+2:]
                res = reducer(sub)
                return res
        return res
    return reducer(_)
   
            

print(reducePath(["NORTH", "WEST", "SOUTH", "EAST"]))
