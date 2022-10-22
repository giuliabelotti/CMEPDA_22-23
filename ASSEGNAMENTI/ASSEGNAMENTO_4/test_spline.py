import unittest
import sys
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

if sys.flags.interactive:
    plt.ion()
from spline2 import ProbabilityDensityFunction

class test(unittest.TestCase):
    """ Unit test con una funzione triangolare
    """
    def triangolare(self):
        x = np.linspace(0., 1, 200)
        y1 = x[0:100]
        y2 = 1 - x[100:200]
        y = np.concatenate((y1, y2))
        pdf = ProbabilityDensityFunction(x, y)

        plt.figure('Sampling')
        plt.hist(pdf.random(50000))

        plt.figure('pdf')
        plt.plot(x, pdf(x))
        plt.xlabel('x')
        plt.ylabel('pdf(x)')

        plt.figure('cdf')
        plt.plot(x, pdf.cdf(x))
        plt.xlabel('x')
        plt.ylabel('cdf(x)')

        plt.figure('ppf')
        xppf = np.linspace(0,0.25,100)
        plt.plot(xppf, pdf.ppf(xppf))
        plt.xlabel('q')
        plt.ylabel('ppf(q)')

        test = pdf.probability(x.min(),x.max())
        print(f"L'area del trinagolo è {test:.2f}")

if __name__ ==  "__main__":
    unittest.main(exit=not sys.flags.interactive)
