__author__ = "Dmitry E. Kislov"
__created__ = "09.01.2019"
__email__ = "kislov@easydan.com"


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

            


    m, n = adj_matrix.shape
    assert m == n, "Illegal adjacency matrix. Adjacency matrix should be of square form."

    vertices = list(range(n))
    selected_edges = []

    
