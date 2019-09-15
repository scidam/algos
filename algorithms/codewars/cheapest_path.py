
class Vertex:
    __slots__ = ('__init__', '__hash__', '__str__', '__repr__', '__eq__', '__sub__', 'x', 'w', 'y', 'previous')
    def __init__(self, x, y, w, previous=None):
        self.x = x
        self.y = y
        self.w = w
        self.previous = previous

    def __hash__(self):
        return hash((self.x, self.y))
    
    def __str__(self):
        return f"({self.x}, {self.y})| {self.w}"

    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, other):
        #  This is very important thing to make dictinary works properly
        return other.x == self.x and other.y == self.y
    
    def __sub__(self, other):
        a, b = self.x - other.x, self.y - other.y
        if a*b != 0:
            raise ValueError("Items should be neighbors")
        if a > 0:
            return "down"
        if a < 0:
            return "up"
        if b > 0:
            return "right"
        if b < 0:
            return "left"

class Distances(dict):
    pass

def get_neighbors(m, v):
    res = list()
    for item in m:
        if v.x + 1 == item.x and v.y == item.y or\
           v.x -1 == item.x and v.y == item.y or\
           v.x == item.x and v.y + 1 == item.y or\
           v.x == item.x and v.y - 1 == item.y:
            res.append(item)
    return res


def dijkstra(mat, sx, sy, ox, oy):
    n, m = len(mat[0]), len(mat)

    unvisited = [Vertex(j, i, mat[j][i]) for i in range(n) for j in range(m)]
    d = Distances()
    path = dict()
    
    for item in unvisited:
        d[item] = 9999
    
    source = Vertex(sx, sy, mat[sx][sy])

    d[source] = 0.0
    
    output = Vertex(ox, oy, mat[ox][oy])

    while output in unvisited:
        minimal = min(filter(lambda x: x in unvisited,  d), key=lambda x: d[x])
        neighbors = get_neighbors(unvisited, minimal)
        unvisited.remove(minimal)
        probe = d[minimal] + mat[minimal.x][minimal.y]
        for item in neighbors:
            if d[item] > probe:
                d[item] = probe
                v = Vertex(item.x, item.y,  probe, previous=minimal)
                path[v] = v
            elif d[item] is None:
                d[item] = d[minimal]
                v = Vertex(item.x, item.y,  d[minimal], previous=minimal)
                path[v] = v
    
    el = output
    res = list()
    while el != source:
        if el in path:
            res.append(Vertex(el.x, el.y, path[el].w))
            el = path[el].previous
        else:
            raise ValueError("Couldn't find a path")


    res.append(source)
    res = res[::-1]
    
    final = list()
    for i, j in zip(range(len(res) -1), range(1, len(res))):
        final.append(res[j]-res[i])

    return final

m = [[1,9,1],
     [2,9,1], 
     [2,1,1]]

v1 = (0,0)
v2 = (0,2)

res = dijkstra(m, *v1, *v2)
print(res)


    
