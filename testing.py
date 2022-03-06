from NFA import NFA
from functions import epsilon
states = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
alphabet = {"a", "b"}
transFunction = {
    0:{

        epsilon:{1, 7}
    },
    1: {
        epsilon:{2, 4}
    },
    2 :{
        "a":{3},

    },
    3: {

        epsilon:{6}
    },
    4:{
        "b":{5},

    },
    5:{

        epsilon: {6},
    },
    6:{

        epsilon: {1,7}
    },
    7:{

        "a":{8},

    },
    8:{
        "b":{9},

    },
    9:{
        "b":{10},

    },
    10:{

    },
}
startState = 0
accpetingStates = {10}
nfa = NFA(states,alphabet,transFunction,startState,accpetingStates)
dfa = nfa.generateDFA()
dfa.clean()
dfa.show()
#Should accept
print("Should accept this strings: ")
print("aaaaaaaaaaaaabb ",dfa.simulate("aaaaaaaaaaaaabb"))
print("aabbaaababababbbbababababb ", dfa.simulate("aabbaaababababbbbababababb"))
print("abb", dfa.simulate("abb"))
#Should not accept
print("Should not accept this strings:")
print("aab ", dfa.simulate("aab"))
print("ab ", dfa.simulate("aab"))
print("a ",dfa.simulate("a"))