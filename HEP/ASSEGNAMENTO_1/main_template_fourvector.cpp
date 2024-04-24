#include "template_fourvector.h"
#include <iostream>

using namespace std;

int main(){

    fourvector<double> p4_a(0,50.,7.,100.);
    fourvector<float> p4_b(0,50.,7.,100.);
    fourvector<double> p4_sum = p4_a + p4_b;
    
    cout << p4_a.Mass() << " " << p4_a.pt() << endl;
    
    cout << p4_sum.px() << "," << p4_sum.py() << "," << p4_sum.pz() << "," << p4_sum.e() << endl;
    
    cout << p4_sum.Mass() << " " << p4_sum.pt() << endl;
   
   
   PtEtaPhiMassVector<double> P1(50,0.5,1.7,10.);
   cout << P1.Theta() << " " << P1.p() << endl; 
    

}
