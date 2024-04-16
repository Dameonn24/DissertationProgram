class TestCase:
    def __init__(self, name, structure): #, variables, actions, assertions):
        self.name = name
        self.structure = structure
        #self.variables = variables
        #self.initialisedVariables = initialisedVariables
        #self.assertions = assertions
    pass

class Variable:
    def __init__(self, name, vId):
        self.name = name
        self.vId = vId
    pass

class Action:
    def __init__(self, name, action, actionValue):
        self.name = name
        self.action = action
        self.actionValue = actionValue
    pass

class Assertion:
    def __init__(self, name, assertion_type, assertion_action, assertion_value):
        self.name = name
        self.assertion_type = assertion_type
        self.assertion_action = assertion_action
        self.assertion_value = assertion_value
    pass