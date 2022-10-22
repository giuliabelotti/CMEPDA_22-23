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
    ''' Classe VoltageData
    '''
    def __init__(self, times, voltages):
        ''' Parametri in ingresso: due iterabili (times e voltages) della stessa lunghezza
        '''
        times = np.array(times, dtype=np.float64)
        voltages = np.array(voltages, dtype=np.float64)
        self.data = np.column_stack([times, voltages])
        self._spline = interpolate.InterpolatedUnivariateSpline(times,
                                                                voltages, k=3)
    @property
    def times(self):
        ''' Slicing syntax per selezionare la prima colonna
        '''
        return self.data[:, 0]

    @property
    def voltages(self):
        ''' Slicing syntax per selezionare la seconda colonna
        '''
        return self.data[:, 1]

    def __getitem__(self, index):
        ''' Square parenthesis syntax
        '''
        return self.data[index]

    def __len__(self):
        ''' Restituisce la il numero di entries
        '''
        return len(self.data)

    def __iter__(self):
        ''' La classe deve essere iterabile
        '''
        return iter(self.data)

    def __str__(self):
        return '\n'.join([f'{i} -> {row[0]: .1f}, {row[1]: .2f}' for i, row in enumerate(self)])

    def __repr__(self):
        '''Stampa il contenuto colonna per colonna
        '''
        return '\n'.join([f'{row[0]: .1f}, {row[1]: .2f}' for row in enumerate(self)])

    def __call__(self, time):
        '''Restituisce il valore interpolato di una tensione ad un dato istante
        '''
        return self._spline(time)

    def plot(self, ax=None, draw_spline=False, **plot_opts):
        '''Disegna il grafico voltages vs times
        '''
        if ax is None:
            plt.figure('voltage_vs_time')
        else:
            plt.sca(ax)
        plt.plot(self.times, self.voltages, label='data', **plot_opts)
        if draw_spline:
            x = np.linspace(min(self.times), max(self.times), 100)
            plt.plot(x, self(x), '-', label='spline')
        plt.xlabel('Time [s]')
        plt.ylabel('Voltage [mV]')
        plt.legend()


if __name__ == "__main__":
    t, v = np.loadtxt('data.txt', unpack=True)
    vdata = VoltageData(t,v)
    print(f'Numero di entries: {len(vdata)}')
    print(vdata[2:10, 0])
    tmp = 0.63
    print(f'Tensione interpolata all\'istante t={tmp}s: {vdata(tmp):.2f}mV')
    vdata.plot(marker='o', linestyle='', color='k', draw_spline=True)
    plt.show()
