
import ROOT

rdf = ROOT.RDataFrame("Events","root://eospublic.cern.ch//eos/root-eos/cms_opendata_2012_nanoaod/Run2012B_DoubleMuParked.root")

#print(rdf.GetColumnNames())

#sel = rdf.Filter("nMuon>0").Filter("Muon_pt[0]>20")

cpp_code = '''
float invMass(float pt1, float eta1, float phi1, float pt2, float eta2, float phi2){
    TLorentzVector mu1, mu2;
    
    mu1.SetPtEtaPhiM(pt1, eta1, phi1, 0.106);
    mu2.SetPtEtaPhiM(pt2, eta2, phi2, 0.106);
    return (mu1+mu2).M();
}
'''

ROOT.gInterpreter.ProcessLine(cpp_code)

sel = rdf.Range(100000).Filter("nMuon>1").Filter("Muon_pt[0]>40").Define("DiMuon_Mass", "invMass(Muon_pt[0], Muon_eta[0], Muon_phi[0],Muon_pt[1], Muon_eta[1], Muon_phi[1])").Filter("Muon_charge[0]*Muon_charge[1]<0")

hist = sel.Histo1D(("DiMuon_Mass","Invariant Mass",100,0,300),"DiMuon_Mass")
hist.Draw()


outCols = ROOT.vector("std::string")()
outCols.push_back("DiMuon_Mass")
outCols.push_back("nMuon")
outCols.push_back("Muon_pt")

sel.Snapshot("Events", "outNtuple.root", outCols)

input()
