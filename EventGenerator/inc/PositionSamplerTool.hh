// art tool to sample starting positions/times, according to some rule
// Ed Callaghan, 2024

#ifndef EventGenerator_PositionSamplerTool_hh
#define EventGenerator_PositionSamplerTool_hh

// stl
#include <utility>
#include <vector>

// art
#include "art/Framework/Principal/Event.h"
#include "art/Framework/Services/Optional/RandomNumberGenerator.h"

// canvas
#include "canvas/Persistency/Common/Ptr.h"

// clhep
#include "CLHEP/Vector/LorentzVector.h"

// mu2e
#include "Offline/MCDataProducts/inc/SimParticle.hh"

namespace mu2e{
  // in general, need to propagate SimParticles back to midstage generators
  // for provenance tracking
  typedef art::Ptr<SimParticle> SimParticlePtr ;
  typedef std::pair<SimParticlePtr,CLHEP::HepLorentzVector> ParticlePositionPair;
  typedef std::vector< SimParticlePtr > SimParticlePtrVector;

  class PositionSamplerTool{
    public:
      PositionSamplerTool(){ /**/ };
      virtual ~PositionSamplerTool(){ /**/ };

      virtual void UseRandomEngine(art::RandomNumberGenerator::base_engine_t&) = 0;
      virtual ParticlePositionPair Sample(const SimParticlePtrVector&) = 0;
    protected:
      /**/
    private:
      /**/
  };
}; // namespace mu2e

#endif
