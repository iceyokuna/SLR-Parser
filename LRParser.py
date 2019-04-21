from Table import Table
from Grammar import Grammar
from StateManager import StateManager

#LR(1) Parser class
class LRParser:
    def __init__(self):
        self.table = Table()
        self.grammar = Grammar()
        #setup as constructor
        self.setup()

    def setup(self):
        self.grammar.setup("grammar.txt")
        stateManager = StateManager(self.grammar)
        stateManager.setup()
        self.table.setup(stateManager)

    #check input string is collect or not (read from input string file)
    def parse(self ,inputString, maximum_step = 99):
        inputQueue = list(inputString)
        inputQueue.append('$')
        stack = [0]
        step = 1
        result = False

        while(step <= maximum_step and result != True):
            if(stack[-1] in self.grammar.getNonterminal()):# case go to
                action = self.table.getGoto(stack[-2], stack[-1]) #2 top of stack
                print("Step : " + str(step) + " Stack: " + str(stack) + " Input: " + str(inputQueue) + " Action : " + str(action))
                stack.append(action[1])
                step += 1
                continue
            #case action
            action = self.table.getAction(stack[-1], inputQueue[0])
            print("Step : " + str(step) + " Stack: " + str(stack) + " Input: " + str(inputQueue) + " Action : " + str(action))
            #check shift || reduce || accept
            if(action[0] == "shift"):
                stack.append(inputQueue.pop(0))
                stack.append(action[1])
            elif(action[0] == "reduce"):
                if(action[1][0] == "accept"):
                    result = True
                reduce_rule = action[1][0]
                reduce_stack_temp = action[1][1].copy()
                reduce_amount = len(reduce_stack_temp) * 2
                for i in range(reduce_amount):
                    stack.pop()
                stack.append(reduce_rule)
            step += 1
        return result

parser = LRParser()
result = parser.parse('cdd')
if(result == 'True'):
    print('accept')
else:
    print('reject')