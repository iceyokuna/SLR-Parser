class SLRMapper:
    def __init__(self):
        self.terminal = {}
        self.nonterminal = {}
        self.grammar = {}

    #not all case (no 'or' case) need grammar loop
    def first(self, grammar):
        for char in grammar:
            if(char in self.terminal):
                return char
            elif(char in self.nonterminal):
                return first(self.grammar[char])
    
    
    def follow(self, grammar):
        pass
        


