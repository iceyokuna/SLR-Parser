from Rule import Rule

class Grammar:
    def __init__(self):
        self.start = ''
        self.nonterminal = set()
        self.terminal = set()
        self.rule = []

    def setup(self):
        #read txt file
        #construct attr
        grammar_file = open("grammar.txt")
        line_count = 0
        for line in grammar_file:
            line = line.strip('\n')
            if(line_count == 0):
                self.start = line.split(' ')[0]
                self.nonterminal = set(line.split(' '))
            elif(line_count == 1):
                self.terminal = set(line.split(' '))
            else:
                rule = Rule()
                rule.setRule(line.split(' '))
                self.rule.append(rule)
            line_count += 1

    def getFirst(self,symbol):
        if symbol in self.terminal:
            return {symbol}
        elif symbol in self.nonterminal:
            r = set()
            for rule in self.rule:
                if(symbol == rule.getName()):
                    r = r.union(self.getFirst(rule.getRule()[0]))
            return r

    def __str__(self):
        temp_str = "Nonterminal\n"
        temp_str += str(self.terminal) + '\n\n'    
        temp_str += "terminal\n"
        temp_str += str(self.nonterminal) + '\n\n'
        temp_str += "start symbol\n"
        temp_str += self.start + '\n\n'
        temp_str += "Rule\n"
        for rule in self.rule:
            temp_str += str(rule) + '\n'
        return temp_str

#g = Grammar()
#g.setup()
#print(g)