
#include <TFile.h>
#include <TTree.h> 
#include <TRandom.h>
#include <TSystem.h>
#include <vector>
#include <iostream>
#include "fourvector.h"

int main() {

    gSystem->Load("AutoDict_FourVector_cxx.so"); //DOBBIAMO CARICARE I DIZIONARI
    gSystem->Load("AutoDict_std__vector_FourVector__cxx.so");
    TFile f("FourVectorTree.root");
    TTree* tree = (TTree*) f.Get("tree");
    auto particles = new std::vector<FourVector>();
   
    tree->SetBranchAddress("particles",(&particles));
    
    for (int i = 0; i <tree->GetEntries(); i++){ 
        tree->GetEntry(i); 
        std::cout << particles->size() << std::endl;  
    }
    
    f.Close();

}
