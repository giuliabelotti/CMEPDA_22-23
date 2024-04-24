
#include "twobodies.h"
#include <iostream>

using namespace std;

int main(){

    Particle pi1(FourVector(0,50.,7.,100.), "Pai1", 100);
    Particle pi2(FourVector(0,50.,7.,100.), "Pai2", 100);

    TwoBodiesDecayedParticle K0s(pi1, pi2, "K0s", 8.9e-11);
    K0s.Class_info();

}
