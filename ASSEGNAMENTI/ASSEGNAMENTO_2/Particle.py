'''
Module: basic Python
Assignment #2 (Set 30, 2021)

--- Goal
Write a program to explore the properties of a few elementary Particles.
The program must contain a Base class Particle and two Child classes, Proton and Alpha, that inherit from it.

--- Specifications
- instances of the class Particle must be initialized with their mass, charge, and name
- the class constructor must also accept (optionally) and store one and only one of the following quantities: energy, momentum, beta or gamma
- whatever the choice, the user should be able to read and set any of the
  above mentioned quantities using just the '.' (dot) operator e.g.
  print(my_particle.energy), my_particle.beta = 0.5
- attempts to set non physical values should be rejected
- the Particle class must have a method to print the Particle information in
  a formatted way
- the child classes Alpha and Protons must use class attributes to store their mass, charge and name
'''
import math

class Particle:
    """ Classe che descrive le particelle
    """
    def __init__(self, mass, charge, name, energy):
        """ Argomenti in ingresso:
            - massa della particella [MeV/c^2]
            - carica della particella (in e)
            - nome della particella
            - energia della particella [MeV/c^2]
        """
        self._mass = mass
        self._charge = charge
        self._name = name
        self._energy = energy

        if self._energy < self._mass:
            print('The energy is lower than the mass!')
            print('energy = mass')
            self._energy = self._mass

    @property
    def mass(self):
        """ Massa della Particella
        """
        return self._mass

    @property
    def charge(self):
        """ Carica della Particella
        """
        return self._charge

    @property
    def name(self):
        """ Nome della Particella
        """
        return self._name

    @property
    def energy(self):
        """ Energia della Particella
        """
        return self._energy

    @energy.setter
    def energy(self, value):
        if value < self.mass:
            print('The energy is lower than the mass!')
            self._energy = self.mass
        else:
            self._energy = value

    @property
    def momentum(self):
        """ Impulso della Particella
        """
        return math.sqrt(self.energy**2 - self.mass**2)

    @momentum.setter
    def momentum(self, value):
        if value < 0:
            print('The momentum is negative!')

        else:
            self._energy = math.sqrt(value**2 + self.mass**2)

    @property
    def beta(self):
        """ Fattore Beta della Particella
        """
        return self.momentum/self._energy

    @beta.setter
    def beta(self, value):
        if value > 1:
            print('beta is > 1!')
            print('beta = 0.99')
            self.beta = 0.99
        else:
            self._energy = self._mass/math.sqrt(1-value**2)

    @property
    def gamma(self):
        """ Fattore Gamma della Particella
        """
        return 1/math.sqrt(1-(self.beta)**2)

    @gamma.setter
    def gamma(self, value):
        if value < 0:
            print('gamma is < 0!')
            print('gamma = 1')
            self.gamma = 1
        else:
            self.energy = self._mass*value


    def information(self):
        """ Stampa informazioni sulla particella
        """
        print(f'Particle Information: \n Name = {self.name} \n Mass = {self.mass} MeV/c^2 \n Charge = {self.charge} e \n Energy = {self.energy} MeV/c^2 \n Momentum = {self.momentum:.3f} MeV/c \n beta = {self.beta:.3f} \n gamma = {self.gamma:.3f}')


class Proton(Particle):
    """ 1° classe che eredita da Particle
    """
    def __init__(self, energy):
        Particle.__init__(self, 938, 1, 'Protone', energy)

class Alpha(Particle):
    """ 2° classe che eredita da Particle
    """
    def __init__(self, energy):
        Particle.__init__(self, 3755.7, 4, 'Alpha', energy)



if __name__ == '__main__':
    p = Proton(1000)
    p.information()
    p.momentum = 100
    p.beta = 0.2
    p.gamma = 1.15

    a = Alpha(4000)
    a.information()
    a.momentum = 300
    a.beta = 0.6
    a.gamma = 1.50
