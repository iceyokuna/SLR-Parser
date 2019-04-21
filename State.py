class State:
    def __init__(self):
        self.state_name = 0 #int
        self.kernal = ()
        self.closure = []

    def setUp(self, grammar):
        self.closure.insert(0,self.kernal)
        #end - no need to do closure
        pointer_location = int(self.kernal[3])
        if(pointer_location >= len(self.kernal[1])):
            print(self.closure)
            return
        if(self.kernal[1][pointer_location] in grammar.getTerminal()):
            print(self.closure)
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
        print(self.closure)

    def setName(self, state_name):
        self.state_name = state_name

    def getName(self):
        return self.state_name

    def setKernal(self, kernal):
        self.kernal = kernal

    def getKernal(self):
        return self.kernal

    def getExpandable(self, grammar):
        expandable_list = []
        for kernal in self.closure:
            pointer_location = kernal[3]
            #check condition : not reach end of kernal
            if(pointer_location < len(kernal[1])):
                temp_kermal = (kernal[0], kernal[1], kernal[2], kernal[3] + 1)
                expandable_list.append(temp_kermal)
        return expandable_list.copy() #return expandable kernal

    def isSameKernal(self, other_kernal):
        return #bool

    def __str__(self):
        return ""