__author__ = "Dmitry E. Kislov"
__created__ = "09.01.2019"
__email__ = "kislov@easydan.com"

import numpy as np

def get_spanning_tree(adj_matrix):
    """Prim's algorithm

    **Parameters**

        :param adj_matrix: NumPy array, a sqaure adjacency matrix 
                           of a graph; each element of the matrix represents
                           weight between corresponding vertices.
        :rtype: list:
        :returns list: a list of vertix numbers

    **Complexity**


    **Links**

    """

    def normalize_edge(edge):
        return (edge[1], edge[0]) if edge[0] > edge[1] else tuple(edge)

    def get_adjacement_vertices(vertix):
        return np.arange(adj_matrix.shape[0])[(adj_matrix[:, vertix] != 0) & ~np.isinf(adj_matrix[:, vertix])]

    def get_adjacement_edges(vertix):
        return [normalize_edge((vertix, v)) for v in get_adjacement_vertices(vertix)]

    def get_minimal_edge(edges):
        edge = np.array(edges)[np.argmin(adj_matrix[i, j] for i, j in edges)]
        return normalize_edge(edge)

    m, n = adj_matrix.shape
    assert m == n, "Illegal adjacency matrix. Adjacency matrix should be of square form."

    vertices = list(range(n))
    done = False
    spanning_tree = []
    
    vertix = vertices.pop()
    edges = get_adjacement_edges(vertix)
    spanning_tree.append(get_minimal_edge(edges))
    spanning_vertices = sum([[i, j] for i, j in spanning_tree], [])

    while set(vertices) - set(spanning_vertices):
        print("Spanning vertices are", spanning_vertices)
        candidate_edges = []
        for vertex in spanning_vertices:
            candidate_edges += [edge for edge in get_adjacement_edges(vertex)]
        candidate_edges = list(filter(lambda x: (x[0] not in spanning_vertices) or (x[1] not in spanning_vertices), candidate_edges))
        print("Candidate edges are", candidate_edges)
        if not candidate_edges:
            print("Spanning tree could not be found. ")
            break
        spanning_tree.append(get_minimal_edge(candidate_edges))
        spanning_vertices = list(set(sum([[i, j] for i, j in  spanning_tree], [])))
    return spanning_tree


if __name__ == '__main__':
    adjacency_matrix = np.array([[0, 2, 4, 1, np.inf],
                                [2, 0, 3, 3, 1],
                                [4, 3, 0, 1, 2],
                                [1, 3, 1, 0, 3],
                                [np.inf, 1, 2, 3, 0]])
    
    print(get_spanning_tree(adjacency_matrix))
