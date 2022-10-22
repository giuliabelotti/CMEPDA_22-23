"""
Module: basic Python
Assignment #4 (October 7, 2021)


--- Goal
Create a ProbabilityDensityFunction class that is capable of throwing
preudo-random number with an arbitrary distribution.

(In practice, start with something easy, like a triangular distribution---the
initial debug will be easier if you know exactly what to expect.)

--- Specifications
- the signature of the constructor should be __init__(self, x, y), where
x and y are two numpy arrays sampling the pdf on a grid of values, that
you will use to build a spline
- [optional] add more arguments to the constructor to control the creation
of the spline (e.g., its order)
- the class should be able to evaluate itself on a generic point or array of
points
- the class should be able to calculate the probability for the random
variable to be included in a generic interval
- the class should be able to throw random numbers according to the distribution
that it represents
- [optional] how many random numbers do you have to throw to hit the
numerical inaccuracy of your generator?
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import InterpolatedUnivariateSpline

class ProbabilityDensityFunction(InterpolatedUnivariateSpline):
    """ Classe PDF che eredita da InterpolatedUnivariateSpline
    """
    def __init__(self, x, y):
        """ Argomenti in ingresso:
            - array x
            - array y
        """
        super().__init__(x, y)
        ycdf = np.array([self.integral(x[0], xcdf) for xcdf in x])
        self.cdf = InterpolatedUnivariateSpline(x, ycdf)
        xppf, ippf = np.unique(ycdf, return_index = True)
        yppf = x[ippf]
        self.ppf = InterpolatedUnivariateSpline(xppf, yppf)
        self.xmax = xppf.max()
        self.xmin = xppf.min()

    def random(self, size):
        """ Lancio di numeri casuali distribuiti con la ppf
        """
        _rand = np.random.uniform(self.xmin, self.xmax, size)
        q  = self.ppf(_rand)
        return q

    def probability(self, x1, x2):
        """ Probabilità che la variabile random sia inclusa in un certo intervallo
        """
        prob = self.cdf(x2) - self.cdf(x1)
        return prob

