#ifndef FOURVECTOR_H
#define FOURVECTOR_H

#include <math.h>

using namespace std;

class FourVector {
	public:
		FourVector() {};
		FourVector(float px, float py, float pz, float E) : m_px(px), m_py(py), m_pz(pz), m_E(E) {};

		float px() const {return m_px;}
		float py() const {return m_py;}
		float pz() const {return m_pz;}
		float E() const {return m_E;}
		
		float Invariant_Mass() const {return sqrt(pow(m_E, 2) - (pow(m_px, 2) + pow(m_py, 2) + pow(m_pz, 2)));}
		float pt() const {return sqrt(pow(m_px,2) + pow(m_py, 2));}
		
		FourVector operator + (FourVector const &other) {
			FourVector sum(m_px+other.m_px, m_py+other.m_py, m_pz+other.m_pz, m_E+other.m_E);
			return sum;		
		}
		
	private:
		float m_px;
		float m_py;
		float m_pz;
		float m_E;
			
};


#endif


