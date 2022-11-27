
#include "FourVector.h"
#include <iostream>


using namespace std;

int main() {
	
	FourVector p4_1(0,50,7.,100.);
	FourVector p4_2(0,50,7.,100.);
	
	cout << p4_1.Invariant_Mass() << " " << p4_1.pt() << endl;
	cout << (p4_1+p4_2).Invariant_Mass() << " " << (p4_1+p4_2).pt() << endl; 
	

}


