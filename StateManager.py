from Grammar import Grammar
from State import State

class StateManager:
    def __init__(self , grammar):
        self.unexpanded_list = []
        self.grammar = grammar
        self.state_list = {}
        self.transition = {}
        self.start = 0
        self.state_count = 0

    def setup(self):
        #set up grammar for this methods
        start_rule = self.grammar.getStartRule()

        #set up start state (set up first closure for start state)
        startState = State()
        startState.setKernal((start_rule[0], start_rule[1],{"$"},0))
        startState.setUp(self.grammar)
        startState.setName(self.state_count)
        self.state_count += 1
        self.state_list[self.start] = startState
        #set up expandable_list with moving pointer
        expandable_list = startState.getExpandable(self.grammar)
        print(expandable_list)
        #start expanding until complete
        while(len(expandable_list) > 0):
            kernal = expandable_list[0]
            state_temp = State()
            state_temp.setKernal((kernal[0], kernal[1], kernal[2], kernal[3]))
            state_temp.setUp(self.grammar)
            for state in self.state_list:
                state_obj = self.state_list[state]
                if(state_temp.getKernal() ==  state_obj.getKernal()):
                    state_temp.setName(state_obj.getName())


                    break

            state_temp.setName(self.state_count)
            self.state_count += 1

    def __str__(self):
        return ""

g = Grammar()
g.setup()
s = StateManager(g)
s.setup()