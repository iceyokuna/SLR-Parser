from Grammar import Grammar
from State import State

class StateManager:
    def __init__(self , grammar):
        self.unexpanded_list = []
        self.grammar = grammar
        self.state_list = []
        self.transition = {}
        self.start = 0
        self.state_count = 0
    
    def getActionFunction(self):
        #Action shift
        actionFunction = {}
        for transition in self.transition:
            if(transition[1] in self.grammar.getTerminal()):
                actionFunction[transition] = ('shift', self.transition[transition].getName())

        #Action Reduce
        for state in self.state_list:
            closure_list = state.getClosure()
            for kernal in closure_list:
                if(kernal[3] == len(kernal[1])): #complete move ex. "AA." len = 2 dot_location = 2
                    for lookahead in list(kernal[2]): # loop every lookahead to create transition
                        if(kernal[0] == self.grammar.getStart()):
                            actionFunction[(state.getName(),lookahead)] = ('reduce', ("Accept",kernal[1]))
                            continue
                        actionFunction[(state.getName(),lookahead)] = ('reduce', (kernal[0],kernal[1]))
        return actionFunction.copy()

    def getGotoFunction(self):
        #Go function
        actionFunction = {}
        for transition in self.transition:
            if(transition[1] in self.grammar.getNonterminal()):
                actionFunction[transition] = ('goto', self.transition[transition].getName())
        return actionFunction.copy()

    def setup(self):
        #set up grammar for this methods
        start_rule = self.grammar.getStartRule()

        #set up start state (set up first closure for start state)
        startState = State()
        startState.setKernal((start_rule[0], start_rule[1],{"$"},0))
        startState.setUp(self.grammar)
        startState.setName(self.state_count)
        self.state_count += 1
        self.state_list.append(startState)
        #set up expandable_list with moving pointer
        expandable_list = startState.getExpandable(self.grammar)
        ##print(expandable_list)
        #start expanding until complete
        
        while(len(expandable_list) > 0):
            kernal = expandable_list[0][1]
            from_state = expandable_list[0][0]
            char_action = kernal[1][kernal[3] - 1]
            state_temp = State()
            state_temp.setKernal((kernal[0], kernal[1], kernal[2], kernal[3]))
            state_temp.setUp(self.grammar)

            if(self.isRepeat(state_temp)):
                state_temp.setName(self.getRepeatId(state_temp))
                self.state_list.append(state_temp)
                self.transition[from_state,char_action] = state_temp
                expandable_list.pop(0)
            else:
                state_temp.setName(self.state_count)
                self.state_list.append(state_temp)
                self.transition[from_state,char_action] = state_temp
                expandable_list.pop(0)
                expandable_list += state_temp.getExpandable(self.grammar)
                self.state_count += 1
        ##print("done")

    def isRepeat(self, kernal_obj):
        for state_obj in self.state_list:
            if(kernal_obj.getKernal() ==  state_obj.getKernal()):
                return True
        return False

    def getRepeatId(self,kernal_obj):
        for state_obj in self.state_list:
            if(kernal_obj.getKernal() ==  state_obj.getKernal()):
                return state_obj.getName()
        return None

#g = Grammar()
#g.setup()
#s = StateManager(g)
#s.setup()
#print(s.getActionFunction())
#print(s.getGotoFunction())