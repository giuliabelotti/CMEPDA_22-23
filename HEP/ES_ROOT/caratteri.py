
#Contare i caratteri di una stringa: JITted header


import ROOT

ROOT.gInterpreter.ProcessLine('#include "caratteri.h"')
s = "Ciao"
n = ROOT.count_characters(s)
print('Il numero di lettere di %s è %i' %(s, n))
