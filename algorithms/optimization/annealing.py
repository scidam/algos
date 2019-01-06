__author__ = "Dmitry E. Kislov"
__created__ = "04.01.2019"
__email__ = "kislov@easydan.com"


import numpy as np


def simulated_annealing(f, bbox, t=lambda t: 1 / t ** 2, threshold=1.0e-8,
                        seed=None):
    """Simulated annealing method.

    **Parameters**

        :param f: a function to be optimized
        :param bbox: an array of size nx2 where n the number of
                     arguments of the function f; each element represents
                     lower and upper bound of the region where the
                     optimum solution should be found
        :param t: temperature function; used to descibe decaying of temperature
        :param threshold: a threshold parameter; if temperature becomes
                          less threshold it is treated as zero
        :param x0: numpy array, initial point where the iteration process starts
        :rtype : numpy array
        :returns: an array, approximate solution of maximization problem

    **Links**
        Almost the same:  https://en.wikipedia.org/wiki/Metropolis%E2%80%93Hastings_algorithm
    """

    def get_candidate_point(bbox):
        bbox = np.array(bbox)
        return np.random.uniform(bbox[:, 0], bbox[:, 1])

    if isinstance(seed, int):
        np.random.seed(seed)
    index = 0
    x = get_candidate_point(bbox)
    temperature = 1
    while temperature > threshold:
        index += 1
        temperature = t(index)
        new_candidate_point = get_candidate_point(bbox)
        diff = f(x) - f(new_candidate_point)
        transition_probability = 1.0 if diff < 0 else np.exp(- diff / temperature)
        if np.random.rand() <= transition_probability:
            x = new_candidate_point
    return x


if __name__ == "__main__":

    # function of one variable
    f = lambda x: np.sin(x)
    bbox = [[0, 2 * np.pi]]

    optimum = simulated_annealing(f, bbox)
    print("Function of one variable: Maximum value is reached at ", optimum, f(optimum))

    # function of two variables

    g = lambda x: np.sin(x[0]) * np.cos(x[1]) + (x[0] + x[1]) ** 2
    bbox = [[0, 2 * np.pi], [0, 2 * np.pi]]

    optimum = simulated_annealing(g, bbox)
    print("Function of two variables: Maximum value is reached at ", optimum, g(optimum))
