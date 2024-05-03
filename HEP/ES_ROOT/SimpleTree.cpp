
#include <TFile.h>
#include <TTree.h> 
#include <TRandom.h> 

int main() {
    TFile f("SimpleTree.root", "RECREATE");
    TTree tree("tree", "My Tree");
    
    double x, y, z, t;
    tree.Branch("x",&x, "x/D");
    tree.Branch("y",&y, "y/D");
    tree.Branch("z",&z, "z/D");
    tree.Branch("t",&t, "t/D");
    
    for (int i = 0; i <128; i++){
        
        x = gRandom->Uniform(-10,10);
        y = gRandom->Gaus(0,5);
        z = gRandom->Exp(10);
        t = gRandom->Landau(0,2);
        tree.Fill();   
    }
    
    tree.Write();
    f.Close();

}
