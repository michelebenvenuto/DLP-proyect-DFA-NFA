from NFA import NFA
from functions import epsilon
states = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
alphabet = {"a", "b"}
transFunction = {
    0:{
        "b":set(),
        "a":set(),
        epsilon:{1, 7}
    },
    1: {
        "a":set(),
        "b":set(),
        epsilon:{2, 4}
    },
    2 :{
        "a":{3},
        "b":set(),
        epsilon:set()
    },
    3: {
        "a":set(),
        "b":set(),
        epsilon:{6}
    },
    4:{
        "b":{5},
        "a":set(),
        epsilon: set(),
    },
    5:{
        "b":set(),
        "a":set(),
        epsilon: {6},
    },
    6:{
        "b":set(),
        "a":set(),
        epsilon: {1,7}
    },
    7:{
        "b":set(),
        "a":{8},
        epsilon:set()
    },
    8:{
        "b":{9},
        "a":set(),
        epsilon: set()
    },
    9:{
        "b":{10},
        "a":set(),
        epsilon: set()
    },
    10:{
        "b":set(),
        "a":set(),
        epsilon: set()
    },
}
startState = 0
accpetingStates = {10}
nfa = NFA(states,alphabet,transFunction,startState,accpetingStates)
dfa = nfa.generateDFA()
print(dfa)
# #Should accept
# print("Should accept this strings: ")
# print("aaaaaaaaaaaaabb ",dfa.simulate("aaaaaaaaaaaaabb"))
# print("aabbaaababababbbbababababb ", dfa.simulate("aabbaaababababbbbababababb"))
# print("abb", dfa.simulate("abb"))
# #Should not accept
# print("Should not accept this strings:")
# print("aab ", dfa.simulate("aab"))
# print("aab ", dfa.simulate("aab"))
# print("a ",dfa.simulate("a"))