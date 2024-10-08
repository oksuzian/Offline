// Sample from multiple event generators, distributed according to material
// isotopic composition
// Ed Callaghan, 2024

// stl
#include <iostream>
#include <map>
#include <string>
#include <utility>

// art
#include "art/Framework/Core/EDProducer.h"
#include "art/Framework/Core/detail/EngineCreator.h"
#include "art/Framework/Principal/Event.h"
#include "art/Framework/Services/Optional/RandomNumberGenerator.h"
#include "art/Framework/Services/Registry/ServiceHandle.h"
#include "art/Utilities/make_tool.h"

// cetlib_except
#include "cetlib_except/exception.h"

// fhiclcpp
#include "fhiclcpp/ParameterSet.h"
#include "fhiclcpp/types/Atom.h"
#include "fhiclcpp/types/Comment.h"
#include "fhiclcpp/types/DelegatedParameter.h"
#include "fhiclcpp/types/Name.h"
#include "fhiclcpp/types/Sequence.h"
#include "fhiclcpp/types/Table.h"

// mu2e
#include "Offline/EventGenerator/inc/ParticleGeneratorTool.hh"
#include "Offline/EventGenerator/inc/PositionSamplerTool.hh"
#include "Offline/MCDataProducts/inc/StageParticle.hh"
#include "Offline/Mu2eG4/inc/ElementSamplerTool.hh"
#include "Offline/Mu2eUtilities/inc/simParticleList.hh"
#include "Offline/SeedService/inc/SeedService.hh"

namespace mu2e{
  class CompositeMaterialGenerator: public art::EDProducer{
    public:
      // sub-config, to affect an element -> generator mapping and specify the
      // configuration of the latter
      struct ElementConfig{
        fhicl::Atom<std::string> name{
          fhicl::Name("name"),
          fhicl::Comment("element identifier")
        };
        fhicl::DelegatedParameter position_tool{
          fhicl::Name("position_tool"),
          fhicl::Comment("ElementSamplerTool configuration")
        };
        fhicl::DelegatedParameter generator_tool{
          fhicl::Name("generator_tool"),
          fhicl::Comment("ParticleGeneratorTool configuration")
        };
      };

      // top-level config, specifying material and sub-configs for each
      // element, as well the elemental weighting scheme and positon/time
      // sampler
      struct Config{
        fhicl::Atom<art::InputTag> spcTag{
          fhicl::Name("SimParticleCollection"),
          fhicl::Comment("InputTag for muon stop SimParticleCollection")
        };
        fhicl::Atom< std::string > processCode{
          fhicl::Name("processCode"),
          fhicl::Comment("Mu2e process code to assign to StageParticle")
        };
        fhicl::DelegatedParameter weighting{
          fhicl::Name("weighting"),
          fhicl::Comment("Configuration to specify how to sample elements from the material")
        };
        fhicl::Sequence< fhicl::Table<ElementConfig> > elements{
          fhicl::Name("elements"), fhicl::Comment("Sequence of tables {\"element\": name, \"position_tool\": PositionSamplerTool, \"generator_tool\": ParticleGeneratorTool configuration}")
        };
      };

      using Parameters = art::EDProducer::Table<Config>;
      CompositeMaterialGenerator(const Parameters&);
      void verify_elements_match();

      virtual void produce(art::Event&) override;
    protected:
      bool _verified_elements;
      art::InputTag _spcTag;
      ProcessCode _processCode;
      art::RandomNumberGenerator::base_engine_t& _engine;
      using ESTPtr = std::unique_ptr<ElementSamplerTool>;
      ESTPtr _element_sampler;
      using PGTPtr = std::unique_ptr<ParticleGeneratorTool>;
      using PSTPtr = std::unique_ptr<PositionSamplerTool>;
      using PSTPGTPtrPair = std::pair<PSTPtr,PGTPtr>;
      using PSTPGTPtrPairMap = std::map<std::string, PSTPGTPtrPair>;
      PSTPGTPtrPairMap _tools;
    private:
      /**/
  };

  CompositeMaterialGenerator::CompositeMaterialGenerator(const Parameters& config):
      art::EDProducer{config},
      _verified_elements(false),
      _spcTag(config().spcTag()),
      _processCode(ProcessCode::findByName(config().processCode())),
      _engine{createEngine(art::ServiceHandle<SeedService>()->getSeed())}{

    // first, instantiate the element sampler
    auto element_config = config().weighting.get<fhicl::ParameterSet>();
    _element_sampler = art::make_tool<ElementSamplerTool>(element_config);
    _element_sampler->UseRandomEngine(_engine);

    // then, construct mapping of element names -> ParticleGeneratorTools
    // as well mapping of element names -> PositionSamplerTools
    auto elements = config().elements();
    for (const auto& element: elements){
      std::string name = element.name();
      auto position_config = element.position_tool.get<fhicl::ParameterSet>();
      auto position_tool = art::make_tool<PositionSamplerTool>(position_config);
      position_tool->UseRandomEngine(_engine);

      auto generator_config = element.generator_tool.get<fhicl::ParameterSet>();
      auto generator_tool = art::make_tool<ParticleGeneratorTool>(generator_config);
      // dummy argument because material is not actually needed in this context
      generator_tool->finishInitialization(_engine, "");

      // enforce that keys to subgenerators are unique
      // would be better in a protected class, but eh
      if (_tools.count(name) == 0){
        _tools[name] = std::make_pair(std::move(position_tool),
                                      std::move(generator_tool));
      }
      else{
        std::string msg = "attempt to override ParticleGeneratorTool key: "
                        + name;
        throw cet::exception("CompositeMaterialGenerator") << msg << std::endl;
      }
    }

    this->produces<StageParticleCollection>();
  }

  void CompositeMaterialGenerator::verify_elements_match(){
    // finally, check that the elements configured with generators
    // are the same elements which comprise the composite material
    // must call a sample here to fake the sampler into post-initializing
    _element_sampler->Sample();
    auto sampled = _element_sampler->Elements();
    std::vector<std::string> defined;
    for (const auto& pair: _tools){
      auto name = pair.first;
      defined.push_back(name);
    }
    if (sampled.size() != defined.size()){
      std::string msg = "# of elements defined in G4Material != # of defined generators ("
                      + std::to_string(sampled.size())
                      + " != "
                      + std::to_string(defined.size())
                      + ")";
      throw cet::exception("CompositeMaterialGenerator") << msg << std::endl;
    }
    std::sort(sampled.begin(), sampled.end());
    std::sort(defined.begin(), defined.end());
    auto pair = std::mismatch(sampled.begin(), sampled.end(), defined.begin());
    if (pair.first != sampled.end()){
      std::string msg = "mismatch between elements of G4Material and elements with defined generators";
      throw cet::exception("CompositeMaterialGenerator") << msg << std::endl;
    }
  }

  void CompositeMaterialGenerator::produce(art::Event& event){
    if (!_verified_elements){
      this->verify_elements_match();
      _verified_elements = true;
    }

    // check that there are muons to sample from...
    auto handle = event.getValidHandle<SimParticleCollection>(_spcTag);
    if (handle->size() < 1){
      std::string msg = "no stopped muons (+/-) from input";
      throw cet::exception("CompositeMaterialGenerator")
              << msg << std::endl;
    }

    // ...and if so, filter and cast into std::vector<art::Ptr<>>
    auto stopped = stoppedMuMinusList(handle);
    if (stopped.size() < 1){
      std::string msg = "no stopped muons (-) from input";
      throw cet::exception("CompositeMaterialGenerator")
              << msg << std::endl;
    }

    // now, sample which element to defer to
    auto element = _element_sampler->Sample();
    auto& tools = _tools[element];
    auto& position_sampler = tools.first;
    auto& generator = tools.second;

    // then, call that element's associated tools:
    // to sample the starting position/time...
    auto pair = position_sampler->Sample(stopped);
    auto sim = pair.first;
    auto fourpos = pair.second;
    // ...and to generate a daughter particle
    auto kinematics = generator->generate();
    auto kinematic = kinematics[0];

    // finally, insert the generated particle into the event
    auto pdg = kinematic.pdgId;
    auto momentum = kinematic.fourmom;
    auto position = fourpos.vect();
    auto time = fourpos.t();
    auto collection = std::make_unique<StageParticleCollection>();
    collection->emplace_back(sim, _processCode, pdg, position, momentum, time);
    event.put(std::move(collection));
  }
}; // namespace mu2e

DEFINE_ART_MODULE(mu2e::CompositeMaterialGenerator)
