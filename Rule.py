class Rule:
    def __init__(self):
        self.rule_name = ""
        self.rule = []

    def setRule(self, rule):
        self.rule_name = rule[0]
        self.rule = rule[1:]

    def getName(self):
        return self.rule_name

    def getRule(self):
        return self.rule

    def __str__(self):
        return self.rule_name + " -> " + str(self.rule)