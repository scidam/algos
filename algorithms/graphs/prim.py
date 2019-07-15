__author__ = "Dmitry E. Kislov"
__created__ = "09.01.2019"
__email__ = "kislov@easydan.com"

import numpy as np


def get_spanning_tree(adj_matrix):
    """Prim's algorithm for finding minimal spanning tree of a graph.

    **Parameters**

        :param adj_matrix: NumPy array, a sqaure adjacency matrix
                           of a graph; each element of the matrix represents
                           weight between corresponding vertices.
        :rtype: list
        :returns list: a list of edges form the minimal spanning tree

    **Complexity**
        Naive implementation: :math:`O(V^2)`

    **Links**
        https://en.wikipedia.org/wiki/Prim%27s_algorithm
    """

    def normalize_edge(edge):
        return (edge[1], edge[0]) if edge[0] > edge[1] else tuple(edge)

    def get_adjacement_vertices(vertix):
        return np.arange(adj_matrix.shape[0])[(adj_matrix[:, vertix] != 0) & ~np.isinf(adj_matrix[:, vertix])]

    def get_adjacement_edges(vertix):
        return [normalize_edge((vertix, v)) for v in get_adjacement_vertices(vertix)]

    def get_minimal_edge(edges):
        edge = np.array(edges)[np.argmin([adj_matrix[i, j] for i, j in edges])]
        return normalize_edge(edge)

    m, n = adj_matrix.shape
    assert m == n, "Illegal adjacency matrix. Adjacency matrix should be of square form."

    vertices = list(range(n))
    spanning_tree = []
    vertix = vertices.pop()
    edges = get_adjacement_edges(vertix)
    spanning_tree.append(get_minimal_edge(edges))
    spanning_vertices = sum([[i, j] for i, j in spanning_tree], [])
    while set(vertices) - set(spanning_vertices):
        candidate_edges = []
        for vertex in spanning_vertices:
            candidate_edges += [edge for edge in get_adjacement_edges(vertex)]
        candidate_edges = list(filter(lambda x: (x[0] not in spanning_vertices) or (x[1] not in spanning_vertices), candidate_edges))
        if not candidate_edges:
            print("Spanning tree could not be found. ")
            return list()
        spanning_tree.append(get_minimal_edge(candidate_edges))
        spanning_vertices = list(set(sum([[i, j] for i, j in spanning_tree], [])))
    return spanning_tree


if __name__ == '__main__':
    adjacency_matrix = np.array([[0, 4, 4, 1, np.inf],
                                [2, 0, 3, 3, 1],
                                [4, 3, 0, 1, 2],
                                [1, 3, 1, 0, 3],
                                [np.inf, 1, 2, 3, 0]])

    print("Weighted adjacency matrix:\n", adjacency_matrix)
    print("Minimal spanning tree: ", get_spanning_tree(adjacency_matrix))

    print("One vertix is leaved out. ")
    adjacency_matrix = np.array([[0, np.inf, np.inf, np.inf, np.inf],
                                [np.inf, 0, 3, 3, 1],
                                [np.inf, 3, 0, 1, 2],
                                [np.inf, 3, 1, 0, 3],
                                [np.inf, 1, 2, 3, 0]])
    print("Minimal spanning tree: ", get_spanning_tree(adjacency_matrix))
