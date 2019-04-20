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
            if(line_count == 0):
                self.start = line.split(' ')[0]
                self.nonterminal = set(line.split(' '))
            elif(line_count == 1):
                self.terminal = set(line.split(' '))
            else:
                self.rule.append(line.split(''))
            line_count += 1

    def getFirst(self, rule_name):
        #get first of rule_name
        pass

    def __str__(self):
        pass