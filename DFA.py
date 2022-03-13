from FA import FA
from pythomata import SimpleDFA

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
    def graph(self):
        dfa = SimpleDFA(self.states, self.alphabet,self.startState, self.accpetingStates,self.transF)
        digraph = dfa.to_graphviz()
        digraph.render("dfa-render") 