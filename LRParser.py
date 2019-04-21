from Table import Table
from Grammar import Grammar
from StateManager import StateManager

#LR(1) Parser class
class LRParser:
    def __init__(self):
        self.table = Table()
        self.setup()

    def setup(self):
        grammar = Grammar()
        grammar.setup("grammar.txt")
        stateManager = StateManager(grammar)
        stateManager.setup()
        self.table.setup(stateManager)

    #check input string is collect or not (read from input string file)
    def parse(self):
        pass


parser = LRParser()