class FA():
    def __init__(self, states ,alphabet, transF, startState, acceptingStates):
        self.states = states
        self.alphabet = alphabet
        self.transF = transF
        self.startState = startState
        self.accpetingStates = acceptingStates

    #simulation function for both DFA AND NFA
    def simulate(self,chars):
        pass

    def move(self,state, char):
        return self.transF[state][char]

"""
Transition function V1
{
    state:{
        char: states
        char: states
        .
        .
        .
    }
    state:{
        char: states
        char: states
        .
        .
        .
    }
    .
    .
    .
}
"""