import FWCore.ParameterSet.Config as cms


from Configuration.GenProduction.PythiaUESettings_cfi import *
source = cms.Source("PythiaSource",
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    maxEventsToPrint = cms.untracked.int32(0),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    comEnergy = cms.untracked.double(10000.0),
    crossSection = cms.untracked.double(1.151),
    PythiaParameters = cms.PSet(
        pythiaUESettingsBlock,
        processParameters = cms.vstring('PMAS(6,1)=172.3 ! t quark mass', 
            'PMAS(347,1)= 750.0 ! graviton mass', 
            'PARP(50)=0.54  ! c(k/Mpl) * 5.4', 
            'MSEL=0         ! User defined processes', 
            'MSUB(391)=1    ! ffbar->G*', 
            'MSUB(392)=1    ! gg->G*', 
            '5000039:ALLOFF ! Turn off graviton decays', 
            '5000039:ONIFANY 6 ! graviton decays into top', 
            '24:ALLOFF ! Turn off W decays', 
            '24:ONIFANY 1 2 3 4 5 6 ! W decays to quarks', 
            'CKIN(3)=25.    ! Pt hat lower cut', 
            'CKIN(4)=-1.    ! Pt hat upper cut', 
            'CKIN(13)=-10.  ! etamin', 
            'CKIN(14)=10.   ! etamax', 
            'CKIN(15)=-10.  ! -etamax', 
            'CKIN(16)=10.   ! -etamin'),
        parameterSets = cms.vstring('pythiaUESettings', 
            'processParameters')
    )
)

configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.2 $'),
    annotation = cms.untracked.string('PYTHIA6-RS750 to tt to jet+MET at 10TeV'),
    name = cms.untracked.string('$Source: /cvs_server/repositories/CMSSW/CMSSW/Configuration/GenProduction/python/Configuration/GenProduction/python/PYTHIA6_Exotica_RS750_tt_jetMET_10TeV_cff.py,v $')
)

