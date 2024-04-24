
#ifndef FOURVECTOR_H
#define FOURVECTOR_H
#include <math.h>

template <class T>
class fourvector {
    
    public: 
        fourvector() {}
        fourvector(T px, T py, T pz, T e) : m_px(px), m_py(py), m_pz(pz), m_e(e) {}
        
        T px() const {return m_px;}
        T py() const {return m_py;}
        T pz() const {return m_pz;}
        T e() const {return m_e;}
        T pt() const {return sqrt(pow(m_px,2) + pow(m_py,2));}
        T Mass() const {return sqrt(pow(m_e,2) - (pow(m_px,2) + pow(m_py,2) + pow(m_pz,2)));}
        
        template <class U>
        fourvector<T> operator + (const fourvector<U> & other) {
            fourvector<T> sum(m_px+other.px(), m_py+other.py(), m_pz+other.pz(), m_e+other.e());
            return sum;
        }
        
      
    private:
        T m_px;
        T m_py;
        T m_pz;
        T m_e;

};


template <class T>
class PtEtaPhiMassVector {

    public:
        PtEtaPhiMassVector() {}
        PtEtaPhiMassVector(T Pt, T Eta, T Phi, T Mass) : m_Pt(Pt), m_Eta(Eta), m_Phi(Phi), m_Mass(Mass) {}
        

        T Pt() const {return m_Pt;}
        T Eta() const {return m_Eta;}
        T Phi() const {return m_Phi;}
        T Mass() const {return m_Mass;}
      
        T Trasvers_Energy() const {return sqrt(pow(m_Pt,2) + pow(m_Mass,2)); }
        T Theta() const { return (2.)*atan(exp(-m_Eta)); }
        T p() const {return m_Pt/sin(Theta()); }
        
     private:
        T m_Pt;
        T m_Eta;
        T m_Phi;
        T m_Mass;

};







#endif





