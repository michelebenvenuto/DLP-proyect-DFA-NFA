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
#TESTING THE DFA THAT ACCPETS (a|b)*abb
states = {0, 1, 2,3}
alphabet = {"a", "b"}
transFunction = {
    0:{
        "b":0,
        "a":1
    },
    1: {
        "a":1,
        "b":2
    },
    2 :{
        "a":1,
        "b":3,
    },
    3: {
        "a":1,
        "b":0
    }
}
startState = 0
accpetingStates = {3}
dfa = DFA(states,alphabet,transFunction,startState,accpetingStates)
#Should accept
print("Should accept this strings: ")
print("aaaaaaaaaaaaabb ",dfa.simulate("aaaaaaaaaaaaabb"))
print("aabbaaababababbbbababababb ", dfa.simulate("aabbaaababababbbbababababb"))
print("abb", dfa.simulate("abb"))
#Should not accept
print("Should not accept this strings:")
print("aab ", dfa.simulate("aab"))
print("aab ", dfa.simulate("aab"))
print("a ",dfa.simulate("a"))
