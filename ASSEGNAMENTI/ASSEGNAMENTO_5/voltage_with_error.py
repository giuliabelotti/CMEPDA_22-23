'''
Module: advanced Python
Assignment #5 (October 18, 2021)

- [optional] support a third optional column for the voltage errors
'''

import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate


class VoltageData:
    ''' Classe VoltageData with voltage errors
    '''
    def __init__(self, times, voltages, voltage_err=None):
        ''' Parametri in ingresso: due iterabili (times e voltages) della stessa lunghezza
        '''
        times = np.array(times, dtype=np.float64)
        voltages = np.array(voltages, dtype=np.float64)
        self.data = np.column_stack((times, voltages))
        if voltage_err is None:
            print('Voltage_err are not present. Only two columns')

        else:
            voltage_err = np.array(voltage_err, dtype=np.float64)
            self.data = np.column_stack((self.data, voltage_err))

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

    @property
    def voltage_err(self):
        ''' Slicing syntax per selezionare la terza colonna
        '''
        try:
            return self.data[:, 2]
        except IndexError:
            err_msg = 'The third column is not present'
            raise AttributeError(err_msg)

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
        try:
            return '\n'.join([f'{i} -> {row[0]: .1f}, {row[1]: .2f}, {row[2]: .2f}' for i, row in enumerate(self)])
        except IndexError:
            print('The third column is not present')
            return '\n'.join([f'{i} -> {row[0]: .1f}, {row[1]: .2f}' for i, row in enumerate(self)])

    def __repr__(self):
        '''Stampa il contenuto colonna per colonna
        '''
        try:
            return '\n'.join([f'{row[0]: .1f}, {row[1]: .2f}, {row[2]: .2f}' for row in enumerate(self)])
        except IndexError:
            print('The third column is not present')
            return '\n'.join([f'{i} -> {row[0]: .1f}, {row[1]: .2f}' for i, row in enumerate(self)])


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
        try:
            plt.errorbar(self.times, self.voltages, self.voltage_err, label='data', **plot_opts)
        except IndexError:
            print('Plot without errorbars')
            plt.plot(self.times, self.voltages, label='data', **plot_opts)
        if draw_spline:
            x = np.linspace(min(self.times), max(self.times), 100)
            plt.plot(x, self(x), '-', label='spline')
        plt.xlabel('Time [s]')
        plt.ylabel('Voltage [mV]')
        plt.legend()


if __name__ == "__main__":
    columns = np.loadtxt('data_with_error.txt', unpack=True)
    vdata = VoltageData(*columns)
    print(vdata)
    print(f'Numero di entries: {len(vdata)}')
    tmp = 0.63
    print(f'Tensione interpolata all\'istante t={tmp}s: {vdata(tmp):.2f}mV')
    vdata.plot(marker='o', linestyle='', color='k', draw_spline=True)
    plt.show()
