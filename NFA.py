from DFA import DFA
from FA import FA
from functions import *
import string

#WAITING FOR THE DEFINITION OFF FUNCTIONS IN FILE functions
class NFA(FA):    
    def simulate(self,chars):
        pass

    def generateDFA(self):
        Dstates = set()
        Dtran = {}
        Dstates.add(epsilonClosureState(self, self.startState))
        DstartState = list(Dstates)[0]
        ## Construcción de subconjuntos
        unmarkedStates = list(Dstates)
        while(len(unmarkedStates) != 0):
            T = unmarkedStates.pop(0)
            print("Curr state: ", T)
            for a in self.alphabet:
                U = epsilonClosureSet(self,moveF(self,T, a))
                if (U not in Dstates):
                    Dstates.add(U)
                    unmarkedStates.append(U)
                if T in Dtran.keys(): 
                    Dtran[T][a] = U
                else:
                    Dtran[T] = {}
                    Dtran[T][a] = U
                
        #Some changes to return de DFA
        DstartState = list(Dstates)[0]
        Dalphabet = self.alphabet
        DfinalStates = set()
        for stateSet in Dstates:
            for state in stateSet:
                if state in self.accpetingStates:
                    DfinalStates.add(stateSet)
        return DFA(Dstates,Dalphabet,Dtran, DstartState,DfinalStates) 