import re

class Automaton:

    def __init__(self, states, initial):
        self.states = states
        self.initial = initial
        self.current = initial
        self.total = 0
    
    def process(self, input):

        for w in input:
            #print(w)
            if w.upper() == "ON":
                self.current = "ON"
            elif w.upper() == "OFF":
                self.current = "OFF"
            elif w == "=":
                print("Total da Soma: " + str(self.total))
            elif re.match(r'\d+', w) and self.current == "ON":
                self.total += int(w)


states = {"ON", "OFF"}
expressions = re.compile(r'\d+|\bON\b|\bOFF\b|=', re.IGNORECASE)

automaton = Automaton(states, "ON")

with open("input.txt", "r") as file:
    automaton.process(expressions.findall(file.read()))