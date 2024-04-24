
#ifndef TWOBODIES_H
#define TWOBODIES_H

#include "Particle.h"
#include <iostream>
#include  <string>
using namespace std;


class TwoBodiesDecayedParticle : public Particle {
    
    public:
        TwoBodiesDecayedParticle() {};
        TwoBodiesDecayedParticle(Particle & pi1, Particle & pi2, string id, float tau) {
            FourVector K0s = pi1 + pi2;
            m_px = K0s.px();
            m_py = K0s.py();
            m_pz = K0s.pz();
            m_E = K0s.E();
            m_id = id;
            m_tau = tau;
            m_pi1 = pi1;
            m_pi2 = pi2;        
        }
        
        
        void Class_info() { 
        
            cout << "The particle is a: " << id() << endl;
            cout << "Invariant mass: " << Invariant_Mass() << endl;
            
            }
       
    private:
        Particle m_pi1;
        Particle m_pi2;                
};

#endif

