
import ROOT

c = ROOT.TCanvas('c1', 'Histogram', 200, 10, 700, 500)

h = ROOT.TH1F("h", "h", 64, -4,4)
h.FillRandom("gaus")
h.Draw()

f = ROOT.TF1("g", "gaus", -8,8)
f.SetParameters(250,0,1)
c.Draw()
f.Draw('same')
