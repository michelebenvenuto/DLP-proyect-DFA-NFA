
epsilon = "ε"

def epsilonClosureState(NFA, state):
    to_return = set()
    #ADD the starting state to the e-closure
    to_return.add(state)
    visited = [state]
    to_check = [state]
    while len(to_check) != 0:
        currState = to_check.pop(0)
        reachableWithEpsilon = NFA.transF[currState][epsilon]
        for s in reachableWithEpsilon:
            if s not in visited:
                to_check.append(s)
                to_return.add(s)
        visited.append(currState)
    return frozenset(to_return)

def epsilonClosureSet(NFA, T):
    to_return = set()
    for state in T:
        eClosure = epsilonClosureState(NFA, state)
        for s in eClosure:
            to_return.add(s)
    return frozenset(to_return)

def moveF(NFA, T, char):
    to_return = set()
    for state in T:
        states = NFA.transF[state][char]
        for s in states:
            to_return.add(s)
    return frozenset(to_return)
