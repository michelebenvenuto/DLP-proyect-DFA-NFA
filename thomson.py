from NFA import NFA
from functions import epsilon, combineTransF

class Thomson():
    def __init__(self, regex):
        self.regex = regex
        self.nextSimbol = 0    
    # Functions to create NFAs of the simple regular expresions 
    def getSimbol(self):
        to_return = self.nextSimbol
        self.nextSimbol += 1
        return to_return

    def simbolNFA(self,char):
        firstSimbol = self.getSimbol()
        secondSimbol = self.getSimbol()
        states = set([firstSimbol, secondSimbol])
        if char ==epsilon:
            alphabet = set()
        else:
            alphabet = set(char)
        initialState = firstSimbol
        finalStates = set([secondSimbol])
        transF = {
            firstSimbol:{
                char:set([secondSimbol])
            },
            secondSimbol:{
            }
        }
        return NFA(states,alphabet, transF,initialState, finalStates)

    def orNFA(self, nfaA, nfaB):
        initialStateSimbol = self.getSimbol()
        finalStateSimbol = self.getSimbol()
        newtransF = combineTransF(nfaA.transF, nfaB.transF)
        newtransF[initialStateSimbol] = {epsilon: set([nfaA.startState, nfaB.startState])}

        for state in nfaA.accpetingStates:
            newtransF[state][epsilon] = set([finalStateSimbol])
        for state in nfaB.accpetingStates:
            newtransF[state][epsilon] = set([finalStateSimbol])
            
        newtransF[finalStateSimbol] = {}
        newStates = nfaA.states | nfaB.states 
        newStates.add(initialStateSimbol)
        newStates.add(finalStateSimbol)
        newAlphabet = nfaA.alphabet | nfaB.alphabet         
        return NFA(newStates, newAlphabet, newtransF, initialStateSimbol, set([finalStateSimbol]))
    
    def concatNFA(self, nfaA, nfaB):
        newTransF = combineTransF(nfaA.transF, nfaB.transF)
        for state in nfaA.accpetingStates:
            newTransF[state][epsilon] = set([nfaB.startState])
        newStates = nfaA.states | nfaB.states
        newAlphabet = nfaA.alphabet | nfaB.alphabet
        return NFA(newStates,newAlphabet, newTransF,nfaA.startState, nfaB.accpetingStates)
    
    def kleenNFA (self, nfaA):
        initialSateSimbol = self.getSimbol()
        finalStateSimbol = self.getSimbol()
        newTransF = nfaA.transF
        newTransF[initialSateSimbol] = {}
        newTransF[initialSateSimbol][epsilon] = set([nfaA.startState, finalStateSimbol])
        newTransF[finalStateSimbol] = {}
        for state in nfaA.accpetingStates:
            newTransF[state][epsilon] = set([nfaA.startState, finalStateSimbol])
        nfaA.states.add(initialSateSimbol)
        nfaA.states.add(finalStateSimbol)
        return NFA(nfaA.states, nfaA.alphabet, newTransF, initialSateSimbol, set([finalStateSimbol]))

    

# thomson = Thomson("asdas")
# nfaA = thomson.simbolNFA("a")
# nfaB = thomson.simbolNFA("b")
# # print("Or DFA")
# # nfaOr = thomson.orNFA(nfaA, nfaB)
# # dfa = nfaOr.generateDFA()
# # dfa.clean()
# # dfa.show()
# print("Concat DFA")

# nfaConcat = thomson.concatNFA(nfaA, nfaB)
# nfaConcat.show()
# dfa = nfaConcat.generateDFA()
# dfa.clean()
# dfa.show()

# print("kleen NFA and DFA")
# nfaKleen = thomson.kleenNFA(nfaA)
# nfaKleen.show()
# dfa = nfaKleen.generateDFA()
# dfa.clean()
# dfa.show()

    
