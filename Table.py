from StateManager import StateManager

class Table:
    def __init__(self):
        self.action = {}
        self.goto = {}
    
    def setup(self, StateManager):
        self.action = StateManager.getActionFunction()
        self.goto = StateManager.getGotoFunction()
        print(self.action)
        print(self.goto)

    def getAction(self, state, action):
        action = self.action[(state, action)]
        return action

    def getGoto(self, state, action):
        goto = self.goto[(state, action)]
        return goto