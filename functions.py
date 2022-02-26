epsilon = "ε"

def epsilonClosureState(NFA, state):
    states = set()
    states.add(state)
    return states | NFA.transFunction[state][epsilon]

def epsilonClosureSet(NFA, T):
    to_return = set()
    for state in T:
        to_return | epsilonClosureSet(NFA, state)
    return to_return
