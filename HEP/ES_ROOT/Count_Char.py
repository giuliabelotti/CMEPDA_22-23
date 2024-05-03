#Contare i caratteri di una stringa: Library loading

import ROOT

# Load a C++ library
ROOT.gInterpreter.ProcessLine('#include "Count_Char.h"')
ROOT.gSystem.Load('./Count_Char.so')


s = "Ciao"
n = ROOT.Count_Char(s)
print('Il numero di lettere di %s è %i' %(s, n))

