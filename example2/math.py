"""
A file for executing math functions
"""

import numpy as np

def one(n = 10):
    """
    a strange function with an ambiguous name

    Parameters
    ----------
    :param n: int
        the number of points to test
    """

    sum = 0.0
    for i in range(n):
        denom = 1.0

    sum += 1/n

    return sum

def pi(npts = 1000):
    """This function caclulates the approximate value of :math:`{\pi}` by stocastic area sampeling.

    Parameters
    ----------
    npts : int
        the number of points to test

    Returns
    -------
    pi_value : float
        the approximated value of :math:`{\pi}`
    """

    bin = 0

    for i in range(npts):

        x = np.random.rand()
        y = np.random.rand()
        r = np.sqrt(x*x + y*y)
        if(r < 1.0):
            bin += 1

    return 4.0 * (bin / npts)
