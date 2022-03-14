from FA import FA
from pythomata import SimpleDFA

class DFA(FA):
    def simulate(self,chars):
        s = self.startState
        for i in range(len(chars)):
            c = chars[i]
            if c not in self.alphabet:
                return False
            s = self.move(s,c)
        if s in self.accpetingStates:
            return True
        else:
            return False