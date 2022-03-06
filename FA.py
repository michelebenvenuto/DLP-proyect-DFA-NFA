import string
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
    
    # Clean the transition funciton of an Automata
    # Usefull when generating a FA from another structure (NFA or regex)
    def clean(self):
        alphabet = list(string.ascii_uppercase)
        curr_keys = self.transF.keys()
        keys_to_letters = {}
        for key in curr_keys:
            letter = alphabet.pop(0)
            keys_to_letters[key] = letter 
        newTransF = {}
        for key in curr_keys:
            newTransF[keys_to_letters[key]] = {}
            for char in self.transF[key].keys():
                newTransF[keys_to_letters[key]][char] = keys_to_letters[self.transF[key][char]]
        self.transF = newTransF
        newStates = set()
        for state in self.states:
            newStates.add(keys_to_letters[state])
        self.states = newStates
        newAcceptingStates = set()
        for state in self.accpetingStates:
            newAcceptingStates.add(keys_to_letters[state])
        self.accpetingStates = newAcceptingStates
        self.startState = keys_to_letters[self.startState]

    def show(self):
        print("States:")
        print(self.states)
        print("Alphabet:")
        print(self.alphabet)
        print("Transition Funtion:")
        print(self.transF)
        print("Start State:")
        print(self.startState)
        print("Accpeting States:")
        print(self.accpetingStates)

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