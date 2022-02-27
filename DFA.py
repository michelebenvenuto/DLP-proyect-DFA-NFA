from FA import FA

class DFA(FA):
    def simulate(self,chars):
        s = self.startState
        for i in range(len(chars)):
            c = chars[i]
            s = self.move(s,c)
        if s in self.accpetingStates:
            return True
        else:
            return False
