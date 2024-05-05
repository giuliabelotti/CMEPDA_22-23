//////////////////////////////////////////////////////////
// This class has been automatically generated on
// Sat May  4 11:23:10 2024 by ROOT version 6.26/02
// from TTree tree/My Tree
// found on file: FourVectorTree.root
//////////////////////////////////////////////////////////

#ifndef TestTree_h
#define TestTree_h

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>

// Header file for the classes stored in the TTree if any.

class TestTree {
public :
   TTree          *fChain;   //!pointer to the analyzed TTree or TChain
   Int_t           fCurrent; //!current Tree number in a TChain

// Fixed size dimensions of array or collections stored in the TTree if any.
   static constexpr Int_t kMaxparticles = 58;

   // Declaration of leaf types
   Int_t           particles_;
   Float_t         particles_m_px[kMaxparticles];   //[particles_]
   Float_t         particles_m_py[kMaxparticles];   //[particles_]
   Float_t         particles_m_pz[kMaxparticles];   //[particles_]
   Float_t         particles_m_E[kMaxparticles];   //[particles_]

   // List of branches
   TBranch        *b_particles_;   //!
   TBranch        *b_particles_m_px;   //!
   TBranch        *b_particles_m_py;   //!
   TBranch        *b_particles_m_pz;   //!
   TBranch        *b_particles_m_E;   //!

   TestTree(TTree *tree=0);
   virtual ~TestTree();
   virtual Int_t    Cut(Long64_t entry);
   virtual Int_t    GetEntry(Long64_t entry);
   virtual Long64_t LoadTree(Long64_t entry);
   virtual void     Init(TTree *tree);
   virtual void     Loop();
   virtual Bool_t   Notify();
   virtual void     Show(Long64_t entry = -1);
};

#endif

#ifdef TestTree_cxx
TestTree::TestTree(TTree *tree) : fChain(0) 
{
// if parameter tree is not specified (or zero), connect the file
// used to generate this class and read the Tree.
   if (tree == 0) {
      TFile *f = (TFile*)gROOT->GetListOfFiles()->FindObject("FourVectorTree.root");
      if (!f || !f->IsOpen()) {
         f = new TFile("FourVectorTree.root");
      }
      f->GetObject("tree",tree);

   }
   Init(tree);
}

TestTree::~TestTree()
{
   if (!fChain) return;
   delete fChain->GetCurrentFile();
}

Int_t TestTree::GetEntry(Long64_t entry)
{
// Read contents of entry.
   if (!fChain) return 0;
   return fChain->GetEntry(entry);
}
Long64_t TestTree::LoadTree(Long64_t entry)
{
// Set the environment to read one entry
   if (!fChain) return -5;
   Long64_t centry = fChain->LoadTree(entry);
   if (centry < 0) return centry;
   if (fChain->GetTreeNumber() != fCurrent) {
      fCurrent = fChain->GetTreeNumber();
      Notify();
   }
   return centry;
}

void TestTree::Init(TTree *tree)
{
   // The Init() function is called when the selector needs to initialize
   // a new tree or chain. Typically here the branch addresses and branch
   // pointers of the tree will be set.
   // It is normally not necessary to make changes to the generated
   // code, but the routine can be extended by the user if needed.
   // Init() will be called many times when running on PROOF
   // (once per file to be processed).

   // Set branch addresses and branch pointers
   if (!tree) return;
   fChain = tree;
   fCurrent = -1;
   fChain->SetMakeClass(1);

   fChain->SetBranchAddress("particles", &particles_, &b_particles_);
   fChain->SetBranchAddress("particles.m_px", particles_m_px, &b_particles_m_px);
   fChain->SetBranchAddress("particles.m_py", particles_m_py, &b_particles_m_py);
   fChain->SetBranchAddress("particles.m_pz", particles_m_pz, &b_particles_m_pz);
   fChain->SetBranchAddress("particles.m_E", particles_m_E, &b_particles_m_E);
   Notify();
}

Bool_t TestTree::Notify()
{
   // The Notify() function is called when a new file is opened. This
   // can be either for a new TTree in a TChain or when when a new TTree
   // is started when using PROOF. It is normally not necessary to make changes
   // to the generated code, but the routine can be extended by the
   // user if needed. The return value is currently not used.

   return kTRUE;
}

void TestTree::Show(Long64_t entry)
{
// Print contents of entry.
// If entry is not specified, print current entry
   if (!fChain) return;
   fChain->Show(entry);
}
Int_t TestTree::Cut(Long64_t entry)
{
// This function may be called from Loop.
// returns  1 if entry is accepted.
// returns -1 otherwise.
   return 1;
}
#endif // #ifdef TestTree_cxx
