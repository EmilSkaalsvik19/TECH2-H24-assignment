"""
TECH2 mandatory assignment - Part A

Write the implementation of part A of the exercise below.
"""

from math import sqrt

def std_loops(x):
    """
    Compute standard deviation of x using loops.

    Parameters
    ----------
    x: Sequence of numbers

    Returns
    -------
    sd : float
        Standard deviation of the list of numbers.
    """
    
    
    "Computing the mean and the square mean using for-loop"
    sum = 0
    square_sum = 0
    for i, item in enumerate(x):
        sum += item
        square_sum += item**2

        "Check if item is the last in the list. This is done by trying to access the next item in the list, and if that fails: you know it is the end"
        try:
            x[i+1]
        except IndexError:
            mean = sum/(i+1)
            square_mean = square_sum/(i+1)
            
    
    variance = square_mean - mean**2
    sd = variance**0.5

    return sd


def std_builtin(x):
    """
    Compute standard deviation of x using the built-in functions sum()
    and len().

    Parameters
    ----------
    x: Sequence of numbers

    Returns
    -------
    sd : float
        Standard deviation of the list of numbers.
    """

    mean = sum(x)/len(x)
    square_mean = (sum(item**2 for item in x))/len(x)

    variance = square_mean - mean**2
    
    sd = sqrt(variance)

    return sd
    