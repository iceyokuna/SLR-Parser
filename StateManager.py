from Grammar import Grammar
from State import State

class StateManager:
    def __init__(self , grammar):
        self.grammar = grammar
        self.state_list = []
        self.transition = {}
        self.start = '0'
        self.state_count = 0
        self.unexpanded_list = []

    def setUp(self):
        grammar_list = self.grammar.getRuleList()
        startState = State()

    def __str__(self):
        return ""