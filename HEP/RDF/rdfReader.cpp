#include <ROOT/RDataFrame.hxx>
#include <TH1D.h>


auto rdfReader() {
    auto rdf = ROOT::RDataFrame("ntuple", "hsimple.root");
    auto h = rdf.Filter("px>py").Histo1D({"pz","hist",10, -2, 2}, "pz");

    
    return h;
}
