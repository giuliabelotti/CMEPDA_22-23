
import ROOT

ROOT.gSystem.Load("AutoDict_FourVector_cxx.so")
ROOT.gSystem.Load("AutoDict_std__vector_FourVector__cxx.so")



f = ROOT.TFile.Open("FourVectorTree.root")

for evt in f.tree:
    for p in evt.particles:
        print(p.E())
        
