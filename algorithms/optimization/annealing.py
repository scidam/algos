__author__ = "Dmitry E. Kislov"
__created__ = "04.01.2019"
__email__ = "kislov@easydan.com"



def simulated_annealing(f, x0,  t=lambda t: 1 / t ** 2, threshold=1.0e-8, seed=None):
    """Simulated annealing method

    **Parameters**

        :param f: a function to be optimized
        :param t: temperature function; used to descibe decaying of temperature
        :param threshold: a threshold parameter; if temperature becomes
                          less threshold it is treated as zero
        :param x0: numpy array, initial point where the iteration process starts
        :rtype : numpy array
        :returns: an array, approximate solution of minization problem

    **Links**

        Link goes here...
    """
    import random

    if isinstance(seed, int):
        random.seed(seed)

    while t > threshold:
        u = random.random()
        
