
import ROOT
import array as arr


c = ROOT.TCanvas('c1', 'c1', 200, 10, 700, 500)
n = 3

x = arr.array('i', [1, 2, 3])
y = arr.array('i', [0, 3, 4])

g = ROOT.TGraph(n,x,y)

g.SetTitle("My graph; myX; myY")
g.SetLineColor(ROOT.kOrange)
g.SetLineWidth(2)
g.SetMarkerStyle(ROOT.kFullSquare)
g.SetMarkerColor(ROOT.kRed)
g.Draw("APL")
c.Draw()
