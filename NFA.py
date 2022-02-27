from DFA import DFA
from FA import FA
from functions import *
import string

#WAITING FOR THE DEFINITION OFF FUNCTIONS IN FILE functions
class NFA(FA):    
    def simulate(self,chars):
        pass

    def generateDFA(self):
        usable_state_names = list(string.ascii_uppercase)
        Dstates = set()
        Dtran = {}
        Dstates.add(epsilonClosureState(self, self.startState))
        DstartState = list(Dstates)[0]
        ## Construcción de subconjuntos
        unmarkedStates = list(Dstates)
        while(len(unmarkedStates) != 0):
            T = unmarkedStates.pop(0)
            print("Curr state: ", T)
            stateName = usable_state_names.pop(0)
            for a in self.alphabet:
                U = epsilonClosureSet(self,moveF(self,T, a))
                if (U not in Dstates):
                    Dstates.add(U)
                    unmarkedStates.append(U)
            if stateName in Dtran.keys(): 
                Dtran[stateName][a] = U
            else:
                Dtran[stateName] = {}
                Dtran[stateName][a] = U
        #Some changes to return de DFA
        DstartState = list(Dstates)[0]
        Dalphabet = self.alphabet
        DfinalStates = set()
        for stateSet in Dstates:
            for state in stateSet:
                if state in self.accpetingStates:
                    DfinalStates.add(stateSet)
        return DFA(Dstates,Dalphabet,Dtran, DstartState,DfinalStates) 