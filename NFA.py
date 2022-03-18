from tracemalloc import start
from DFA import DFA
from FA import FA
from functions import *
import string
import time
#WAITING FOR THE DEFINITION OFF FUNCTIONS IN FILE functions
class NFA(FA):    
    def simulate(self,chars):
        start_time = time.time()
        S = epsilonClosureState(self, self.startState)
        c = 0
        while(c<len(chars)):
            if chars[c] not in self.alphabet:
                return False, (time.time() - start_time)
            S = epsilonClosureSet(self, moveF(self,S,chars[c]))
            c +=1
        if(len(S & self.accpetingStates) != 0):
            return True, (time.time() - start_time)
        else:
            return False, (time.time() - start_time)

    def generateDFA(self):
        Dstates = set()
        Dtran = {}
        Dstates.add(epsilonClosureState(self, self.startState))
        DstartState = list(Dstates)[0]
        ## Construcción de subconjuntos
        unmarkedStates = list(Dstates)
        while(len(unmarkedStates) != 0):
            T = unmarkedStates.pop(0)
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
        Dalphabet = self.alphabet
        DfinalStates = set()
        for stateSet in Dstates:
            for state in stateSet:
                if state in self.accpetingStates:
                    DfinalStates.add(stateSet)
        return DFA(Dstates,Dalphabet,Dtran, DstartState,DfinalStates) 