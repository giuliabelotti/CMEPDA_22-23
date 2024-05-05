
import ROOT

rdf = ROOT.RDataFrame("ntuple", "hsimple.root")
h = rdf.Filter("px>py").Histo1D(("pz","hist",10, -2, 2), "pz")

h.Draw();

input()
