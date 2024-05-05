import ROOT

rdf = ROOT.RDataFrame("ntuple", "hsimple.root")
h = rdf.Define("somma", "px+py").Histo1D(("somma","hist",10, -2, 2), "somma")

h.Draw();

input()
