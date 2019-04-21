from Grammar import Grammar
from State import State

class StateManager:
    def __init__(self , grammar):
        self.unexpanded_list = []
        self.grammar = grammar
        self.state_list = []
        self.transition = {}
        self.start = '0'
        self.state_count = 0

    def setup(self):
        #set up grammar for this methods
        start_rule = self.grammar.getStartRule()

        #set up start state
        startState = State()
        startState.setName(str(self.state_count))
        startState.setKernal((start_rule[0], start_rule[1],{"$"},0))
        #set up first closure for start state
        startState.setUp(self.grammar)

        #pre condition before setup (add Expandable) #already move pointer -> ready to be kernal
        #Expandable = startState.getExpandable()
        #for kernal in Expandable:
        #    self.unexpanded_list.append(kernal)

    def __str__(self):
        return ""

g = Grammar()
g.setup()
s = StateManager(g)
s.setup()