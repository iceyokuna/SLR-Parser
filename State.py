class State:
    def __init__(self):
        self.state_name = ""
        self.kernal = []
        self.closure = []

    def setUp(self, grammar):
        #end - no need to do closure
        pointer_location = int(self.kernal[3])
        if(pointer_location >= len(self.kernal[2])):
            return
        if(self.kernal[1][pointer_location] in grammar.getTerminal()):
            return
            
        lookahead = self.kernal[2]
        expandable_list = []
        expandable_list.append(self.kernal[1][pointer_location])

        while(len(expandable_list) > 0):
            for rule in grammar.getRule(expandable_list[0]):
                closure_temp = ((rule[0], rule[1], lookahead.copy(), 0))
                self.closure.append(closure_temp)
                #case can expand more
                if(rule[1][0] in grammar.getNonterminal()):
                    expandable_list.append(rule[1][0])
                    #bind a new lookahead for next loop (need some fix)
                    lookahead = grammar.getFirst(rule[1][1])
                #pop from expandable_list
            expandable_list.pop(0)
        print(self.kernal)
        print(self.closure)

    def setName(self, name):
        self.name = name

    def setKernal(self, kernal):
        self.kernal = kernal

    def getExpandable(self):
        return [] #return expandable kernal

    def isSameKernal(self, other_kernal):
        return #bool

    def __str__(self):
        return ""