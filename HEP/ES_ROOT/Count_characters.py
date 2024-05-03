
#Contare i caratteri di una stringa: JITted string

import ROOT

cpp_code = """
    
    int count_characters(const std::string & c ) {
        return c.size();
    }
    
"""

ROOT.gInterpreter.ProcessLine(cpp_code)
s = "Ciao"
n = ROOT.count_characters(s)
print('Il numero di lettere di %s è %i' %(s, n))

