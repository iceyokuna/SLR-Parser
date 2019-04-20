class Rule:
    def __init__(self):
        self.rule_name = ""
        self.rule = []

    def setRule(self, rule):
        self.rule_name = rule[0]
        self.rule = rule[1:]
    
    def getFirst(self):
        #return first of rule locally
        pass