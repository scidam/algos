__author__ = "Dmitry E. Kislov"
__created__ = "26.12.2018"
__email__ = "kislov@easydan.com"


def graham_convex_hull(array):
    '''Graham's scan for convex hull of a set of 2D points

       This algorithm is named after Ronald Graham, who published the original
       algorithm in 1972.

    **Parameters**

        :param array: an array of points [(x1, y1), (x2, y2), ..., (xN, yN)]
        :type array: list
        :rtype: list
        :returns: convex hull presented as a list of points


    **References**

        Graham, R.L. (1972). "An Efficient Algorithm for Determining the Convex
        Hull of a Finite Planar Set" (PDF). Information Processing Letters. 1:
        132–133. doi:10.1016/0020-0190(72)90045-2
    '''
    import math

    EPS = 1.0e-15 # very small number, epsilon1 value
    # the lesser numbers are treated as zero

    if len(array) < 3:
        raise Exception("Input array should have length greater or equal 3.")

    # helper function
    cross_product = lambda p, q: p[0] * q[1] - q[0] * p[1]

    # Additionally, one could perform checking for collinearity here
    if len(array) == 3:
        return array

    # get min index
    ys = list(map(lambda x: x[-1], array))
    y_min_ind = ys.index(min(ys))
    xmin, ymin = array[y_min_ind]

    # create array of angles
    angles = list()
    for x, y in array:
        if abs(x - xmin) > EPS:
            angles.append(math.atan((y - ymin) / (x - xmin)))
        elif abs(x - xmin) < EPS and abs(y - ymin) < EPS:
            angles.append(0.0)
        else:
            angles.append(math.pi / 2.0)

        if angles[-1] < -EPS:
            # ensure that all atan values are in [0, pi]
            angles[-1] = math.pi - angles[-1]

    # sorting array of angles
    angles_sorted_inds = sorted(range(len(angles)), key=lambda k: angles[k])

    sorted_array = [array[j] for j in angles_sorted_inds]
    stack = list()
    stack.append(sorted_array[0])
    stack.append(sorted_array[1])
    for i in range(2, len(array)):
        c, p, q = stack[-2], stack[-1], sorted_array[i]
        cross_value = cross_product([p[0] - c[0], p[1] - c[1]],
                                    [q[0] - c[0], q[1] - c[1]])
        while len(stack) >= 2 and cross_value <= -EPS:
            stack.pop()
            c, p, q = stack[-2], stack[-1], sorted_array[i]
            cross_value = cross_product([p[0] - c[0], p[1] - c[1]],
                                        [q[0] - c[0], q[1] - c[1]])
        stack.append(q)
    return stack


if __name__ == '__main__':
    test_data = [(2, 4),
                 (1, 5),
                 (2, -1),
                 (7, 3),
                 (5, 4),
                 (2, 1),
                 (7, 0),
                 (3, 1),
                 (4, 0),
                 (3.2, 3)
                 ]
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        plt = None

    if plt:
        print("Lets gonna do some visualization here... ")
        plt.scatter(*zip(*test_data), s=5, marker='o')
        chull = graham_convex_hull(test_data)
        plt.scatter(*zip(*chull), s=10, marker='s')
        plt.show()

    print("=" * 40)
    print("Graham's convex hull is: ", graham_convex_hull(test_data))
    print("=" * 40)
