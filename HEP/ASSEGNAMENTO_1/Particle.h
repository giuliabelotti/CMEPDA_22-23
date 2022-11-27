
#ifndef PARTICLE_H
#define PARTICLE_H

#include <math.h>
#include "FourVector.h"

class Particle : public FourVector {
	public: 
		Particle() {};
		Particle (const FourVector &p4, int pid, float tau) : FourVector(p4), m_pid(pid), m_tau(tau) {};
		int pid() const {return m_pid;}
		float tau() const {return m_tau;}
		
	private:
		int m_pid;
		float m_tau; 

};

#endif
