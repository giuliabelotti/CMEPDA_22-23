
import ROOT

c = ROOT.TCanvas('c1', 'Histogram', 200, 10, 700, 500)

histo = ROOT.TH1F("histo", "histo", 64, 0,16)
histo.FillRandom("pol1")
histo.Draw()

histo.SetLineWidth(4)
histo.SetLineColor(ROOT.kRed)

c.Draw()

