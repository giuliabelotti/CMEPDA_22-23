'''
Module: advanced Python
Assignment #5 (October 18, 2021)

- [optional] rewrite the run_tests() function in sandbox/test_voltage_data.py
  as a sequence of proper UnitTests

'''

import numpy as np
import unittest
from voltage_data_full import VoltageData
import os
from matplotlib import pyplot as plt

class TestVoltageData(unittest.TestCase):
    """ Set up the test
    """
    def setUp(self, sample_size=10):
        self.sample_size = sample_size
        self.t = np.linspace(0., 2., self.sample_size)
        self.v = np.random.uniform(0.5, 1.5, self.sample_size)
        self.v_err = 0.5*np.ones(self.sample_size)
        current_dir = os.getcwd()
        file_name = 'data.txt'
        file_name_with_error = 'data_with_error.txt'
        
        self.sample_file = os.path.join(current_dir, file_name)
        self.sample_file_with_error = os.path.join(current_dir, file_name_with_error)

    def load_from_sample_arrays(self):
        return VoltageData(self.t, self.v), \
               VoltageData(self.t, self.v, self.v_err)
               
    def test_costructor(self):
        voltage, voltage_with_error = self.load_from_sample_arrays()
        self.assertEqual(voltage.data.shape, (self.sample_size, 2))
        self.assertEqual(voltage_with_error.data.shape, (self.sample_size, 3))
    
    def test_from_file(self):
        """Test constructor from file, both with and without the errors."""
        voltage = VoltageData.from_file(self.sample_file)
        voltage_with_error = VoltageData.from_file(self.sample_file_with_error)           
                
    def test_getitem(self):
        """Test __getitem__"""
        voltage, voltage_with_error = self.load_from_sample_arrays()
        self.assertAlmostEqual(voltage[0,0], self.t[0])
        self.assertAlmostEqual(voltage_with_error[0, 2], self.v_err[-1])
        
    def test_formatting(self):
        """Test __str__ ad __repr__"""
        voltage, voltage_with_error = self.load_from_sample_arrays()
        print(voltage, '\n')
        print(repr(voltage), '\n')
        print(voltage_with_error, '\n')
        print(repr(voltage_with_error), '\n')     

    def test_plotting(self, draw=False):
        """ Test plotting."""
        voltage, voltage_with_errs = self.load_from_sample_arrays()
        plt.figure('test_plot')
        ax = plt.gca()
        voltage.plot(ax)
        voltage_with_errs.plot(ax, fmt='r*')
        if draw:
            plt.show()

        
if __name__ == "__main__":
    unittest.main()     
       
        
