# Find shortest path in Maze

from queue import Queue

maze =	[
		[ 1, 1, 1, 1, 1, 0, 0, 1, 1, 1 ],
		[ 0, 1, 1, 1, 1, 1, 0, 1, 0, 1 ],
		[ 0, 0, 1, 0, 1, 1, 1, 0, 0, 1 ],
		[ 1, 0, 1, 1, 1, 0, 1, 1, 0, 1 ],
		[ 0, 0, 0, 1, 0, 0, 0, 1, 0, 1 ],
		[ 1, 0, 1, 1, 1, 0, 0, 1, 1, 0 ],
		[ 0, 0, 0, 0, 1, 0, 0, 1, 0, 1 ],
		[ 0, 1, 1, 1, 1, 1, 1, 1, 0, 0 ],
		[ 1, 1, 1, 1, 1, 0, 0, 1, 1, 1 ],
		[ 0, 0, 1, 0, 0, 1, 1, 0, 0, 1 ],
	    ]

m = len(maze)
n = len(maze[0])

def get_available_positions(M, x):
    i, j = x
    all = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
    m = len(M)
    n = len(M[0])
    all = filter(lambda x: m > x[0] >= 0, all)
    all = filter(lambda x: n > x[1] >= 0, all)
    all = filter(lambda x: M[i][j], all)
    return tuple(all)

q = Queue()
marked = set()
paths = dict()
def shortest_path(M, x):
    i, j = x
    q.put((0, 0))
    marked.add((0, 0))
    while (i, j) not in marked:
        if q.empty():
            print("Target position couldn't be reached")
            return
        previous = q.get()
        positions = get_available_positions(M, previous)
        for pos in positions:
            q.put(pos)
            marked.add(pos)
            current_path = paths.setdefault(pos, list())
            if previous not in current_path:
                current_path.append(previous)

def print_path(current):
    cc = current
    path = '{}'.format(cc)
    while (0, 0) != cc:
        cc = paths[cc][0]
        path += " -> {}".format(cc)
    print(path)

shortest_path(maze, (7, 5))
print_path((7, 5))
