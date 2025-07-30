import ROOT
from analysis import Analysis
from itertools import permutations
from itertools import combinations
import numpy as np


class ExampleHistograms(Analysis.Histograms):
    def create_histograms(self):
        """
        self.hist_MUSIC_5mil_7masses_muon0Pt=ROOT.TH1F("muon0_pt", f'{self.title[12:22]};leading muon p_{{T}} [GeV];a.u.', 50, 0, 500) 
        self.hist_MUSIC_5mil_7masses_muon1Pt=ROOT.TH1F("muon1_pt", f'{self.title[12:22]};subleading muon p_{{T}} [GeV];a.u.', 50, 0, 500) 

        self.hist_MUSIC_5mil_7masses_dimuonPt=ROOT.TH1F("dimuon_pt", f'{self.title[12:22]};di-muon p_{{T}} [GeV];a.u.', 50, 0, 500) 

        self.hist_MUSIC_5mil_7masses_muon1Ptvsmuon0Pt=ROOT.TH2F("muon1vsmuon0_pt", f'{self.title[12:22]};leading muon p_{{T}} [GeV];subleading muon p_{{T}} [GeV];', 50, 0, 500, 50, 0, 500) 
        """
        self.hist_MUSIC_5mil_7masses_any_electronPt=ROOT.TH1F("electron_pt", f'{self.title[12:22]};electron p_{{T}} [GeV];a.u.', 50, 0, 100) 
        self.hist_MUSIC_5mil_7masses_had_electronPt=ROOT.TH1F("electron_pt", f'{self.title[12:22]};electron p_{{T}} [GeV];a.u.', 50, 0, 100) 
        # """
        # Hadronic
        # """
        self.hist_MUSIC_5mil_7masses_had_nJets=ROOT.TH1F("n Jets (hadronic)", f'{self.title[12:22]};Number of jets ;a.u. ', 10, 0, 10)  

        self.hist_MUSIC_5mil_7masses_had_systemM=ROOT.TH1F("WW_mass", f'{self.title[12:22]};WW mass [Gev];a.u. ', 50, 0, 1500) 
        self.hist_MUSIC_5mil_7masses_had_JetPair1_M=ROOT.TH1F("Jetspair_1_M", f'{self.title[12:22]};(Jet pair 1) W M [Gev];a.u. ', 30, 65, 95)  
        self.hist_MUSIC_5mil_7masses_had_JetPair2_M=ROOT.TH1F("Jetspair_2_M", f'{self.title[12:22]};(Jet pair 2) W M [Gev];a.u. ', 30, 65, 95)   
        self.hist_MUSIC_5mil_7masses_all_hadronic_JetPairM=ROOT.TH1F("both_pairs_M", f'{self.title[12:22]};(both Jet pairs) W M [Gev];a.u. ', 30, 65, 95)  
        self.hist_MUSIC_5mil_7masses_had_JetPair1_Pt=ROOT.TH1F("Jetspair_1_Pt", f'{self.title[12:22]};(Jet pair 1) W Pt [Gev];a.u. ', 50, 0, 200)  
        self.hist_MUSIC_5mil_7masses_had_JetPair2_Pt=ROOT.TH1F("Jetspair_2_Pt", f'{self.title[12:22]};(Jet pair 2) W Pt [Gev];a.u. ', 50, 0, 200)  
        self.hist_MUSIC_5mil_7masses_all_hadronic_JetPairPt=ROOT.TH1F("both_pairs_Pt", f'{self.title[12:22]};(both Jet pairs) W Pt [Gev];a.u. ', 50, 0, 100)  # not sure we want this
        self.hist_MUSIC_5mil_7masses_had_Jet1_Pt=ROOT.TH1F("Jet1_Pt", f'{self.title[12:22]};Jet1 Pt [Gev];a.u. ', 50, 0, 200)  
        self.hist_MUSIC_5mil_7masses_had_Jet2_Pt=ROOT.TH1F("Jet2_Pt", f'{self.title[12:22]};Jet2 Pt [Gev];a.u. ', 50, 0, 200)  
        self.hist_MUSIC_5mil_7masses_had_Jet3_Pt=ROOT.TH1F("Jet3_Pt", f'{self.title[12:22]};Jet3 Pt [Gev];a.u. ', 50, 0, 200)  
        self.hist_MUSIC_5mil_7masses_had_Jet4_Pt=ROOT.TH1F("Jet4_Pt", f'{self.title[12:22]};Jet4 Pt [Gev];a.u. ', 50, 0, 200)  
        self.hist_MUSIC_5mil_7masses_had_Jet1_Eta=ROOT.TH1F("Jet1_eta", f'{self.title[12:22]};Jet1 eta [Gev];a.u. ', 50, -5, 5)
        self.hist_MUSIC_5mil_7masses_had_Jet2_Eta=ROOT.TH1F("Jet2_eta", f'{self.title[12:22]};Jet2 eta [Gev];a.u. ', 50, -5, 5)
        self.hist_MUSIC_5mil_7masses_had_Jet3_Eta=ROOT.TH1F("Jet3_eta", f'{self.title[12:22]};Jet3 eta [Gev];a.u. ', 50, -5, 5)
        self.hist_MUSIC_5mil_7masses_had_Jet4_Eta=ROOT.TH1F("Jet4_eta", f'{self.title[12:22]};Jet4 eta [Gev];a.u. ', 50, -5, 5)



        """
        semi-leptonic below
        """
   
        self.hist_MUSIC_5mil_7masses_semilep_nJets=ROOT.TH1F("n Jets (semilep)", f'{self.title[12:22]};Number of jets (semilep) ;a.u. ', 10, 0, 10)  
        
        self.hist_MUSIC_5mil_7masses_semilep_muonPt=ROOT.TH1F("muon_pt", f'{self.title[12:22]};muon p_{{T}} [GeV];a.u.', 50, 0, 100)  
        #self.hist_MUSIC_5mil_7masses_semilep_muonic_channelMt=ROOT.TH1F("mu_vl_Mt", f'{self.title[12:22]};(m and vm) W Mt [Gev];a.u.', 50, 0, 500)  
        self.hist_MUSIC_5mil_7masses_semilep_muonEta=ROOT.TH1F("muon_eta", f'{self.title[12:22]};muon eta [GeV];a.u.', 50, -5, 5) 
        
    
        self.hist_MUSIC_5mil_7masses_semilep_systemPt=ROOT.TH1F("WW_pt", f'{self.title[12:22]};WW Pt [Gev];a.u. ', 50, 0, 500) 
        self.hist_MUSIC_5mil_7masses_semilep_systemMt=ROOT.TH1F("WW_Mt", f'{self.title[12:22]};WW Mt [Gev];a.u. ', 50, 0, 1000) 
        self.hist_MUSIC_5mil_7masses_semilep_electronPt=ROOT.TH1F("electron_pt", f'{self.title[12:22]};electron p_{{T}} [GeV];a.u.', 50, 0, 100)   
        self.hist_MUSIC_5mil_7masses_semilep_electronEta=ROOT.TH1F("electron_eta", f'{self.title[12:22]};electron eta [GeV];a.u.', 50, -5, 5)
        #self.hist_MUSIC_5mil_7masses_semilep_electron_channelMt=ROOT.TH1F("e_vl_Mt", f'{self.title[12:22]};(e and ve) W Mt [Gev];a.u.', 50, 0, 500)  
            
        self.hist_MUSIC_5mil_7masses_semilep_leptonPt=ROOT.TH1F("lepton_pt", f'{self.title[12:22]};lepton p_{{T}} [GeV];a.u.', 50, 0, 100)   
        self.hist_MUSIC_5mil_7masses_semilep_leptonEta=ROOT.TH1F("lepton_eta", f'{self.title[12:22]};lepton eta [GeV];a.u.', 50, -5, 5)
        #self.hist_MUSIC_5mil_7masses_semilep_missingET=ROOT.TH1F("missingET", f'{self.title[12:22]};missingET [Gev];a.u.', 50, 0, 200)  

        self.hist_MUSIC_5mil_7masses_semilep_Jet1M=ROOT.TH1F("Jet1_M", f'{self.title[12:22]};leading Jet M [Gev];a.u.', 30, 65, 95) 
        self.hist_MUSIC_5mil_7masses_semilep_Jet2M=ROOT.TH1F("Jet2_M", f'{self.title[12:22]};subleading Jet M [Gev];a.u.', 30, 65, 95) 
        self.hist_MUSIC_5mil_7masses_semilep_total_JetM=ROOT.TH1F("combinedJets_M", f'{self.title[12:22]};(combined Jets) W Mass [Gev];a.u.', 30, 65, 95)  
        self.hist_MUSIC_5mil_7masses_semilep_total_JetPt=ROOT.TH1F("combinedJets_Pt", f'{self.title[12:22]};(combined Jets) W Pt [Gev];a.u.', 50, 0, 200)  
        #self.hist_MUSIC_5mil_7masses_semilep_leptonic_channelPt=ROOT.TH1F("l_vl_pt", f'{self.title[12:22]};(l and v) W p_{{T}} [GeV];a.u.', 50, 0, 500)  
        #self.hist_MUSIC_5mil_7masses_semilep_leptonic_channelMt=ROOT.TH1F("l_vl_Mt", f'{self.title[12:22]};(l and v) W Mt [Gev];a.u.', 50, 0, 500)  
            
        """
        Leptonic
        """
        self.hist_MUSIC_5mil_7masses_leptonic_ee_electron1Pt=ROOT.TH1F("electron1_pt", f'{self.title[12:22]};leading electron p_{{T}} [GeV];a.u.', 40, 20, 60)  
        self.hist_MUSIC_5mil_7masses_leptonic_ee_electron2Pt=ROOT.TH1F("electron2_pt", f'{self.title[12:22]};subleading electron p_{{T}} [GeV];a.u.', 40, 20, 60)  
        self.hist_MUSIC_5mil_7masses_leptonic_ee_electron1Eta=ROOT.TH1F("electron1_eta", f'{self.title[12:22]};leading electron eta ;a.u.', 50, -5, 5)
        self.hist_MUSIC_5mil_7masses_leptonic_ee_electron2Eta=ROOT.TH1F("electron2_eta", f'{self.title[12:22]};subleading electron eta ;a.u.', 50, -5, 5)
       
    
        self.hist_MUSIC_5mil_7masses_leptonic_emu_muonPt=ROOT.TH1F("muon_pt", f'{self.title[12:22]};muon p_{{T}} [GeV];a.u.', 50, 0, 100)  
        self.hist_MUSIC_5mil_7masses_leptonic_emu_electronPt=ROOT.TH1F("electron_pt", f'{self.title[12:22]};electron p_{{T}} [GeV];a.u.', 50, 0, 100)  
        self.hist_MUSIC_5mil_7masses_leptonic_emu_muonEta=ROOT.TH1F("muon_eta", f'{self.title[12:22]};muon eta ;a.u.', 50, -5, 5)
        self.hist_MUSIC_5mil_7masses_leptonic_emu_electronEta=ROOT.TH1F("electron_eta", f'{self.title[12:22]};electron eta ;a.u.', 50, -5, 5)
        
        
        self.hist_MUSIC_5mil_7masses_leptonic_mm_muon1Pt=ROOT.TH1F("muon1_pt", f'{self.title[12:22]};leading muon p_{{T}} [GeV];a.u.', 50, 0, 100)  
        self.hist_MUSIC_5mil_7masses_leptonic_mm_muon2Pt=ROOT.TH1F("muon2_pt", f'{self.title[12:22]};subleading muon p_{{T}} [GeV];a.u.', 50, 0, 100)
        self.hist_MUSIC_5mil_7masses_leptonic_mm_muon1Eta=ROOT.TH1F("muon_eta", f'{self.title[12:22]};leading muon eta ;a.u.', 50, -5, 5)
        self.hist_MUSIC_5mil_7masses_leptonic_mm_muon2Eta=ROOT.TH1F("muon_eta", f'{self.title[12:22]};subleading muon eta ;a.u.', 50, -5, 5)
        
        #self.hist_MUSIC_5mil_7masses_leptonic_missingET=ROOT.TH1F("missingET", f'{self.title[12:22]};missingET [Gev];a.u.', 50, 0, 200)  
        
        self.hist_MUSIC_5mil_7masses_leptonic_lepton1Pt=ROOT.TH1F("lepton1_pt", f'{self.title[12:22]};lepton1 p_{{T}} [GeV];a.u.', 50, 0, 100) 
        self.hist_MUSIC_5mil_7masses_leptonic_lepton2Pt=ROOT.TH1F("lepton2_pt", f'{self.title[12:22]};lepton 2 p_{{T}} [GeV];a.u.', 50, 0, 100) 
        self.hist_MUSIC_5mil_7masses_leptonic_lepton1Eta=ROOT.TH1F("lepton1_Eta", f'{self.title[12:22]};lepton1 Eta;a.u.', 50, -5, 5)
        self.hist_MUSIC_5mil_7masses_leptonic_lepton2Eta=ROOT.TH1F("lepton2_Eta", f'{self.title[12:22]};lepton 2 Eta ;a.u.', 50, -5, 5)

        #self.hist_MUSIC_5mil_7masses_leptonic_system_Pt=ROOT.TH1F("sys_Pt", f'{self.title[12:22]};WW Pt [Gev];a.u.', 50, 0, 500)  
        #self.hist_MUSIC_5mil_7masses_leptonic_system_Mt=ROOT.TH1F("sys_Mt", f'{self.title[12:22]};WW Mt [Gev];a.u.', 50, 0, 500)  
        self.hist_MUSIC_5mil_7masses_leptonic_nJets=ROOT.TH1F("n Jets (leptonic)", f'{self.title[12:22]};Number of jets (lep) ;a.u. ', 10, 0, 10)
            
            

    def fill_histograms(self, sample):
        """
        self.hist_MUSIC_5mil_7masses_muon0Pt.Fill(sample.Muon[0].PT)anni_1__anyDecay_default_1mil_all_hadronic_JetPairM
        self.hist_MUSIC_5mil_7masses_muon1Pt.Fill(sample.Muon[1].PT)

        self.hist_MUSIC_5mil_7masses_muon1Ptvsmuon0Pt.Fill(sample.Muon[0].PT,sample.Muon[1].PT)

        # Add muons using pT
        dimuon=sample.Muon[0].P4()+sample.Muon[1].P4()
        self.hist_MUSIC_5mil_7masses_dimuonPt.Fill(dimuon.Pt())

        """
        """
        hadronic
        """
        if len(sample.Electron) >= 0:
            for i in range(len(sample.Electron)):
                electron = sample.Electron[i].P4()
                self.hist_MUSIC_5mil_7masses_any_electronPt.Fill(electron.Pt())
        # # print(len(sample.Muon))
        # if len(sample.JetPF) == True:
        #     sample.Jet = []
        #     sample.Jet = sample.JetPF
        if len(sample.Jet) >= 4:
            if len(sample.Electron) >= 0:
                for i in range(len(sample.Electron)):
                    electron = sample.Electron[i].P4()
                    self.hist_MUSIC_5mil_7masses_had_electronPt.Fill(electron.Pt())
            Jet1 = sample.Jet[0].P4()
            Jet2 = sample.Jet[1].P4()
            Jet3 = sample.Jet[2].P4()
            Jet4 = sample.Jet[3].P4()
        #if hadronic == True:
            self.hist_MUSIC_5mil_7masses_had_Jet1_Pt.Fill(Jet1.Pt())
            self.hist_MUSIC_5mil_7masses_had_Jet2_Pt.Fill(Jet2.Pt())
            self.hist_MUSIC_5mil_7masses_had_Jet3_Pt.Fill(Jet3.Pt())
            self.hist_MUSIC_5mil_7masses_had_Jet4_Pt.Fill(Jet4.Pt())
            self.hist_MUSIC_5mil_7masses_had_Jet1_Eta.Fill(Jet1.Eta())
            self.hist_MUSIC_5mil_7masses_had_Jet2_Eta.Fill(Jet2.Eta())
            self.hist_MUSIC_5mil_7masses_had_Jet3_Eta.Fill(Jet3.Eta())
            self.hist_MUSIC_5mil_7masses_had_Jet4_Eta.Fill(Jet4.Eta())
            
            self.hist_MUSIC_5mil_7masses_had_nJets.Fill(len(sample.Jet))       
            indexList = list(range(len(sample.Jet)))
            
            JetPairs = list(permutations(indexList, 2)) #just a list of indices

            #Array of sum of 2 Jets, their overall P4, then their index tuple
            sumArr = [[sample.Jet[a].P4() + sample.Jet[b].P4() for (a, b) in JetPairs],
                        [(a, b) for (a, b) in JetPairs]] 

            #list of sum of 2 Jets, their overall P4, then their index tuple
            masses = [item.M() for item in sumArr[0]] #list of .M() for all in sumArr
            wMass = float(self.title[:7])
            
            diff = list(zip([abs(mass - wMass) for mass in masses], JetPairs))
            
            min_sum = float('inf')
            best_combo = None

            for i in range(len(diff)):
                for j in range(len(diff)):
                    mass_diff1 = diff[i][0]
                    Jets1 = diff[i][1]
                    mass_diff2 = diff[j][0]
                    Jets2 = diff[j][1]
                    
                    if set(Jets1).isdisjoint(Jets2):
                        total_diff = mass_diff1 + mass_diff2
                        if total_diff < min_sum:
                            min_sum = total_diff
                            best_combo = (Jets1, Jets2) 
                            indices = (i, j)
            k, l = indices
            jetPair1 = sumArr[0][k]
            jetPair2 = sumArr[0][l]
            #figure out how to add 5th jet to 2nd pair if it exists... hmmmmmmmm
            #need to get from Jets1, Jets2, the jet that is not included, sample.Jet[x]
            #JEts1 is the 2 indices. Same as JEts2.
            if set(range(5)).isdisjoint(Jets2) and set(range(5)).isdisjoint(Jets1):
                set(Jets1).update(set(Jets2))
                thirdIndex = set(range(5)).difference(set(Jets1))
                
                jetPair2 = jetPair2 + sample.Jet[thirdIndex.pop()].P4()

            self.hist_MUSIC_5mil_7masses_had_JetPair1_M.Fill(jetPair1.M())
            self.hist_MUSIC_5mil_7masses_had_JetPair2_M.Fill(jetPair2.M())
            self.hist_MUSIC_5mil_7masses_had_JetPair1_Pt.Fill(jetPair1.Pt())
            self.hist_MUSIC_5mil_7masses_had_JetPair2_Pt.Fill(jetPair2.Pt())

            self.hist_MUSIC_5mil_7masses_all_hadronic_JetPairM.Fill(jetPair1.M())
            self.hist_MUSIC_5mil_7masses_all_hadronic_JetPairM.Fill(jetPair2.M())
            self.hist_MUSIC_5mil_7masses_all_hadronic_JetPairPt.Fill(jetPair1.Pt())
            self.hist_MUSIC_5mil_7masses_all_hadronic_JetPairPt.Fill(jetPair2.Pt())
            
            """
            """
            
            if len(sample.Jet) > 4:
                total_Jets = sample.Jet[0].P4() + sample.Jet[1].P4() + sample.Jet[2].P4() + sample.Jet[3].P4() + sample.Jet[4].P4()
            else:
                total_Jets = sample.Jet[0].P4() + sample.Jet[1].P4() + sample.Jet[2].P4() + sample.Jet[3].P4()
            self.hist_MUSIC_5mil_7masses_had_systemM.Fill(total_Jets.M())
            
            return 

            """
            Semi-leptonic
        #     """
        # if (len(sample.Muon) + len(sample.Electron)) >= 1 and len(sample.JetPF) == True:
        #     sample.Jet = []
        #     sample.Jet = sample.JetPF
        if (len(sample.Muon) + len(sample.Electron)) >= 1 and len(sample.Jet) >= 2 and len(sample.Jet) < 4:
        
            if len(sample.Muon)==1:
                muon = sample.Muon[0].P4()
                if muon.Pt() >= 10:
                    

                #muonic_channel = muon + sample.MissingET[0].P4()
                #self.hist_MUSIC_5mil_7masses_semilep_muonic_channelMt.Fill(muonic_channel.Mt())
                    self.hist_MUSIC_5mil_7masses_semilep_muonPt.Fill(muon.Pt())
                    self.hist_MUSIC_5mil_7masses_semilep_muonEta.Fill(muon.Eta())
                lepton = muon
            elif len(sample.Electron)==1:
                electron = sample.Electron[0].P4()
                if electron.Pt() >= 10:
                    
                #electron_channel = electron + sample.MissingET[0].P4()
                #self.hist_MUSIC_5mil_7masses_semilep_electron_channelMt.Fill(electron_channel.Mt())
                    self.hist_MUSIC_5mil_7masses_semilep_electronPt.Fill(electron.Pt())
                    self.hist_MUSIC_5mil_7masses_semilep_electronEta.Fill(electron.Eta())
                lepton = electron
            else:
                return #False 

            self.hist_MUSIC_5mil_7masses_semilep_nJets.Fill(len(sample.Jet))
            if lepton.Pt() > 10:
                self.hist_MUSIC_5mil_7masses_semilep_leptonPt.Fill(lepton.Pt())
                self.hist_MUSIC_5mil_7masses_semilep_leptonEta.Fill(lepton.Eta())     
            #self.hist_MUSIC_5mil_7masses_semilep_missingET.Fill(sample.MissingET[0].MET)  
            #leptonic_channel = lepton + sample.MissingET[0].P4()
            #self.hist_MUSIC_5mil_7masses_semilep_leptonic_channelPt.Fill(leptonic_channel.Pt())
            #self.hist_MUSIC_5mil_7masses_semilep_leptonic_channelMt.Fill(leptonic_channel.Mt())

            self.hist_MUSIC_5mil_7masses_semilep_Jet1M.Fill(sample.Jet[0].Mass)
            self.hist_MUSIC_5mil_7masses_semilep_Jet2M.Fill(sample.Jet[1].Mass)
            total_Jet = sample.Jet[0].P4() + sample.Jet[1].P4()
            if len(sample.Jet) > 2:
                total_jet = sample.Jet[0].P4() + sample.Jet[1].P4() + sample.Jet[2].P4()
            self.hist_MUSIC_5mil_7masses_semilep_total_JetM.Fill(total_Jet.M())
            self.hist_MUSIC_5mil_7masses_semilep_total_JetPt.Fill(total_Jet.Pt())

            #system = total_Jet + leptonic_channel
            
            #self.hist_MUSIC_5mil_7masses_semilep_systemPt.Fill(system.Pt())
            #self.hist_MUSIC_5mil_7masses_semilep_systemMt.Fill(system.Mt())
            
            #return
            """
            Fully leptonic below
            """
            
        if (len(sample.Muon) + len(sample.Electron))>=2 and len((sample.Jet)) == 0:
            if len(sample.Muon)==0 and len(sample.Electron)>=2:
                electron1 = sample.Electron[0].P4()
                electron2 = sample.Electron[1].P4()
                self.hist_MUSIC_5mil_7masses_leptonic_ee_electron1Pt.Fill(electron1.Pt())
                self.hist_MUSIC_5mil_7masses_leptonic_ee_electron2Pt.Fill(electron2.Pt())
                self.hist_MUSIC_5mil_7masses_leptonic_ee_electron1Eta.Fill(electron1.Eta())
                self.hist_MUSIC_5mil_7masses_leptonic_ee_electron2Eta.Fill(electron2.Eta()) 
                
                lepton1 = electron1
                lepton2 = electron2
                

            elif len(sample.Muon)>=1 and len(sample.Electron)>=1:
                muon = sample.Muon[0].P4()
                electron = sample.Electron[0].P4()
                self.hist_MUSIC_5mil_7masses_leptonic_emu_muonPt.Fill(muon.Pt())
                self.hist_MUSIC_5mil_7masses_leptonic_emu_electronPt.Fill(electron.Pt())
                self.hist_MUSIC_5mil_7masses_leptonic_emu_muonEta.Fill(muon.Eta())
                self.hist_MUSIC_5mil_7masses_leptonic_emu_electronEta.Fill(electron.Eta())
                lepton1 = muon
                lepton2 = electron
                
            elif len(sample.Muon)>=2 and len(sample.Electron)==0:
                muon1 = sample.Muon[0].P4()
                muon2 = sample.Muon[1].P4()
                self.hist_MUSIC_5mil_7masses_leptonic_mm_muon1Pt.Fill(muon1.Pt())
                self.hist_MUSIC_5mil_7masses_leptonic_mm_muon2Pt.Fill(muon2.Pt())
                self.hist_MUSIC_5mil_7masses_leptonic_mm_muon1Eta.Fill(muon1.Eta())
                self.hist_MUSIC_5mil_7masses_leptonic_mm_muon2Eta.Fill(muon2.Eta())
                lepton1 = muon1
                lepton2 = muon2
            
            
            #system = lepton1 + lepton2 + sample.MissingET[0].P4()
            self.hist_MUSIC_5mil_7masses_leptonic_nJets.Fill(len(sample.Jet))
            #self.hist_MUSIC_5mil_7masses_leptonic_missingET.Fill(sample.MissingET[0].MET) 
            self.hist_MUSIC_5mil_7masses_leptonic_lepton1Pt.Fill(lepton1.Pt())
            self.hist_MUSIC_5mil_7masses_leptonic_lepton2Pt.Fill(lepton2.Pt())
            self.hist_MUSIC_5mil_7masses_leptonic_lepton1Eta.Fill(lepton1.Eta())
            self.hist_MUSIC_5mil_7masses_leptonic_lepton2Eta.Fill(lepton2.Eta())
            #self.hist_MUSIC_5mil_7masses_leptonic_system_Pt.Fill(system.Pt())
            #self.hist_MUSIC_5mil_7masses_leptonic_system_Mt.Fill(system.Mt())
            

class ExampleAnalysis(Analysis.Analysis):
    """
    An example analysis that plots the pT of the leading muon.
    """
    def __init__(self):
        super(ExampleAnalysis, self).__init__(ExampleHistograms)

    def selection(self, sample):
        return True

        # if len(sample.Muon)>0:
        #     return True
        # return False
        #return 
        # if len(sample.FatJet) == 1 or len(sample.Jet)==2:
        #     return True
        # return False
        
        #if (len(sample.Muon)+len(sample.Electron))>=1:
         #   return True
        #return False
    #  if len(sample.Muon) >= 1 and len(sample.Jet) >= 2:
    #         return True
    #     return False
        
        # if (len(sample.Muon) + len(sample.Electron))>=2:
        #     return True
        # return False
        # """
        # Hadronic (I think)
        # """
        # if len(sample.Jet) >= 4:
        #    return hadronic == True
        # return hadronic == False
        # """
        # Semi-leptonic (to muon)
        # # """
        # if len(sample.Muon) >= 1 and len(sample.Jet) >= 2:
        #     return semilepMuon == True
        # return semilepMuon == False

        # if len(sample.Electron) >= 1 and len(sample.Jet) >= 2:
        #     return semilepElec == True
        # return semilepElec == False
# tonic_lepton1Eta=ROOT.TH1F("lepton1_Eta", f'{self.title[12:22]};lepton1 Eta;a.u.', 50, -5, 5)
#         self.hist_MUSIC_5mil_7masses_leptonic_lepton2Eta=ROOT.TH1F("lepton2_Eta", f'{self.title[12:22]};lepton 2 Eta ;a.u.', 50, -5, 5)

#         self.hist_MUSIC_5mil_7masses_leptonic_system_Mt=ROOT.TH1F("sys_Mt", f'{self.title[12:22]};WW transverse Mass [Gev];a.u.', 50, 0, 500) 

            
            
        # if (len(sample.Muon) + len(sample.Electron))>=1 and len(sample.Jet) >= 2:
        #     return semilepGen == True
        # return semilepGen == False

