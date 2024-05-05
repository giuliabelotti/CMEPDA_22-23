

#include <TFile.h>
#include <TTree.h> 
#include <TRandom.h>
#include <TSystem.h>
#include <vector>
#include "fourvector.h"

int main() {
    TFile f("FourVectorTree.root", "RECREATE");
    TTree tree("tree", "My Tree");
    
    int nParticles;
    std::vector<FourVector> particles;
   
    gInterpreter->GenerateDictionary("FourVector","fourvector.h");
    gInterpreter->GenerateDictionary("std::vector<FourVector>","fourvector.h");
    
    tree.Branch("particles",&particles);
    
    for (int i = 0; i <100; i++){ //loop on event
        nParticles = gRandom->Uniform(0,30);
        particles.clear();
        particles.resize(nParticles);
        for (int j = 0; j<nParticles; j++){ //loop on particles per event
            particles.push_back(FourVector(gRandom->Gaus(3,2), i, j, j*j));
        }    
        tree.Fill();   
    }
    
    tree.Write();
    f.Close();

}
