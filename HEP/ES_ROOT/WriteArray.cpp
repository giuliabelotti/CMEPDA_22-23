
#include <TFile.h>
#include <TTree.h> 

int main() {
    TFile f("TreeArray.root", "RECREATE");
    TTree tree("tree", "My Tree");
    
    float x[100];
    int n;
    tree.Branch("n",&n, "n/I");
    tree.Branch("myFloats",x, "x[n]/F");
    
    
    for (int i = 0; i <100; i++){ //loop on event
        n = i;
        for (int j = 0; j<n; j++){ //loop on particles per event
            x[j] = i*j;
        }    
        tree.Fill();   
    }
    
    tree.Write();
    f.Close();

}
