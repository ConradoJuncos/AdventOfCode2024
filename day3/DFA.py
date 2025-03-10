class DFA:
    def __init__(self, states, alphabet, transitions, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions  # Dictionary of (state, symbol) -> next_state
        self.current_state = start_state
        self.accept_states = accept_states

    def reset(self):
        self.current_state = start_state

    def process(self, input_string):
        for symbol in input_string:
            if (self.current_state, symbol) in self.transitions:
                self.current_state = self.transitions[(self.current_state, symbol)]
            else:
                return False  # Rejected if no transition is defined

        return self.current_state in self.accept_states  # Accept if in final state

# Example DFA that accepts strings ending in 'ab'
states = {"q0", "q1", "q2"}
alphabet = {"a", "b"}
transitions = {
    ("q0", "a"): "q1",
    ("q1", "b"): "q2",
    ("q2", "a"): "q1",  # Looping back
}
start_state = "q0"
accept_states = {"q2"}

dfa = DFA(states, alphabet, transitions, start_state, accept_states)

# Test
test_string = "abab"
print(dfa.process(test_string))  # True if accepted, False otherwise
