
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
    
    #functions to create the NFA from a regex

    def precedence(self,op):
        if op == '.':
            return 1
        if op == '|':
            return 2
        if op == '*':
            return 3
        return 0

    #create nfa form two nfas and an operation
    def applyOp(self, a,  op, b = None):
        if op == '.': return self.concatNFA(a,b) 
        if op == '|': return self.orNFA(a,b)
        if op == '*': return self.kleenNFA(a)
    
    def createNfafromRegex(self):

        # stack to store the NFAs
        nfas = []
        
        # stack to store Operators 

        ops = []

        i = 0

        regex = self.regex
        while i < len(regex):
            # ignore empty spaces
            if regex[i] == ' ':
                i += 1
                continue
            
            elif regex[i] == '(':
                ops.append(regex[i])
            
            # If we read a letter check if the next char in the 
            # regex is a letter, if it is it means there is a concat
            # operation between the two simbols 
            # NOTE THIS WORKS ONLY BECAUSE WE ARE ONLY READING ONE LETTER AT A TIME
            elif regex[i].isalpha():
                if i + 1< len(regex) and regex[i + 1].isalpha():
                    ops.append('.')
                nfas.append(self.simbolNFA(regex[i]))
            
            elif regex[i] == ')':
                while len(ops) !=0 and ops[-1] != '(':
                    op = ops.pop()
                    if op == "*":
                        nfa1 = nfas.pop()
                        nfas.append(self.applyOp(nfa1, op))
                    else:
                        nfa2 = nfas.pop()
                        nfa1 = nfas.pop()
                        nfas.append(self.applyOp(nfa1, op, nfa2))
                ops.pop()
            else:
                while (len(ops) != 0 and self.precedence(ops[-1]) >= self.precedence(regex[i])):
                    op = ops.pop()
                    if op == "*":
                        nfa1 = nfas.pop()
                        nfas.append(self.applyOp(nfa1, op))
                    else:
                        nfa2 = nfas.pop()
                        nfa1 = nfas.pop()
                        nfas.append(self.applyOp(nfa1, op, nfa2))
                ops.append(regex[i])
            i +=1
        while len(ops) != 0:
            op = ops.pop()
            if op == "*":
                nfa1 = nfas.pop()
                nfas.append(self.applyOp(nfa1, op))
            else:
                nfa2 = nfas.pop()
                nfa1 = nfas.pop()
                nfas.append(self.applyOp(nfa1, op, nfa2))         
        return nfas[-1]

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

thomson = Thomson("(a|b)")
nfa = thomson.createNfafromRegex()    
nfa.show()
dfa = nfa.generateDFA()
dfa.clean()
dfa.show()
#Should accept

