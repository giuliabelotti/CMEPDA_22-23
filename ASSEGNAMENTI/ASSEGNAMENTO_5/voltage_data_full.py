'''
Module: advanced Python
Assignment #5 (October 18, 2021)


--- Goal
Write a class to handle a sequence of voltage measurements at different times.

--- Specifications
- the class name must be VoltgeData
- the class must be initialized with two generic iterables of the same length
  holding the numerical values of times and voltages
- alternatively the class can be initialized from a text file
- the class must expose two attributes: 'times' and 'voltages', each returning
  a numpy array of type numpy.float64 of the corresponding quantity.
- the values should be accessible with the familiar square parenthesis syntax:
  the first index must refer to the entry, the second selects time (0) or
  voltage (1). Slicing must also work.
- calling the len() function on a class instance must return the number of
  entries
- the class must be iterable: at each iteration, a numpy array of two
  values (time and voltage) corresponding to an entry in the file must be
  returned
- the print() function must work on class instances. The output must show one
  entry (time and voltage), as well as the entry index, per line.
- the class must also have a debug representation, printing just the values
  row by row
- the class must be callable, returning an interpolated value of the tension
  at a given time
- the class must have a plot() method that plots data using matplotlib.
  The plot function must accept an 'ax' argument, so that the user can select
  the axes where the plot is added (with a new figure as default). The user
  must also be able to pass other plot options as usual
- [optional] rewrite the run_tests() function in sandbox/test_voltage_data.py
  as a sequence of proper UnitTests
- [optional] support a third optional column for the voltage errors
'''
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

class VoltageData:
    """ Class VoltageData """
    def __init__(self, times, voltages, volt_error=None):
        """ Class constructor. Times and voltages are iterables of the same
        length.
        """
        times = np.array(times, dtype=np.float64)
        voltages = np.array(voltages, dtype=np.float64)
        self.data = np.column_stack((times,voltages))
        if volt_error is not None:
            print('There are three columns!')
            volt_error = np.array(volt_error, dtype=np.float64)
            self.data = np.column_stack((self.data, volt_error))
        self._spline = interpolate.InterpolatedUnivariateSpline(times, voltages, k=3)
        
    @classmethod
    def from_file(cls, file_path):
        print(cls)
        columns = np.loadtxt(file_path, unpack = True)
        return cls(*columns)
               
    @property
    def times(self):
        """ Slice syntax to select the first column
        """
        return self.data[:, 0]
                
    @property
    def voltages(self):
        """ Slice syntax to select the second column
        """
        return self.data[:, 1]
                   
    @property
    def volt_error(self):
        """ Slice syntax to select the third column, if present
        """
        try:
            return self.data[:, 2]            
        except IndexError:
            msg = 'Voltage error are not present!'
            raise AttributeError(msg)
                                       
    def __getitem__(self, index):
        """ Square parenthesis syntax
        """
        return self.data[index]
        
    def __len__(self):
        """ return the number of entries
        """
        return len(self.data)
        
    def __iter__(self):
        """ Class is iterable
        """
        return iter(self.data)
        
    def __str__(self):
        """ The output shows entry index, time and voltage
        """
        try:
            return '\n'.join([f'{i} -> {row[0]: .1f}, {row[1]: .2f}, {row[2]: .2f}' for i, row in enumerate(self)])
        except IndexError:
            print('Only two columns!')
            return '\n'.join([f'{i} -> {row[0]: .1f}, {row[1]: .2f}' for i, row in enumerate(self)])
                    
    def __repr__(self):
        """ Debug representation, printing just the values row by row
        """
        try:
            return '\n'.join([f'{i} -> {row[0]: .1f}, {row[1]: .2f}, {row[2]: .2f}' for i, row in enumerate(self)])
        except IndexError:
            print("There isn't a third column")
            return '\n'.join([f'{i} -> {row[0]: .1f}, {row[1]: .2f}' for i, row in enumerate(self)])
            
    def __call__(self, time):
        """ Return the voltage value interpolated at time t
        """
        return self._spline(time)
        
    def plot(self, ax=None, draw_spline=False, **plot_opts):
        """ Draw the data points
        """
        if ax is None:
            plt.figure('voltage_vs_time')
        else:
            plt.sca(ax)        
        try:
            plt.errorbar(self.times, self.voltages, self.volt_error, label='data', **plot_opts)            
        except AttributeError:
            print('Plot without errorbars')
            plt.plot(self.times, self.voltages, label='data', **plot_opts)
        if draw_spline:
            x = np.linspace(min(self.times), max(self.times), 100)
            plt.plot(x, self(x), '-', label='spline')            
        plt.xlabel('Time [s]')
        plt.ylabel('Voltage [mV]')
        plt.legend()
        
