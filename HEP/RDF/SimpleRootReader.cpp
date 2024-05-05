#include <TFile.h>
#include <TTree.h>
#include <iostream>
#include <TH1F.h>
#include <TCanvas.h>

TH1F * SimpleRootReader() {

    float px,py,pz,random,i;
    
    TH1F* hist = new TH1F("hist", "hist",10, -2, 2);
    
    TFile f("hsimple.root");
    TTree *t = (TTree *) f.Get("ntuple");
    
    t->SetBranchAddress("px", &px);
    t->SetBranchAddress("py", &py);
    t->SetBranchAddress("pz", &pz);
    t->SetBranchAddress("random", &random);
    t->SetBranchAddress("i", &i);
    
    
    //TCanvas *c = new TCanvas("c1", "Histogram", 200, 10, 700, 500);
    
    
    for( int j = 0; j<t->GetEntries(); j++){
        t->GetEntry(j);
        hist->Fill(px);
        //std::cout << px << std::endl;
    
    }
    
    hist->Draw("hist");
    return hist;

}
