class TestCase:
    def __init__(self, name, structure, variables, initialisedVariables, assertions):
        self.name = name
        self.structure = structure
        self.variables = variables
        self.initialisedVariables = initialisedVariables
        self.assertions = assertions
    pass

class Variable:
    def __init__(self, name, vId, action, actionValue):
        self.name = name
        self.vId = vId
        self.action = action
        self.actionValue = actionValue
    pass

class InitialisedVariable:
    def __init__(self, name, action, actionValue):
        self.name = name
        self.action = action
        self.actionValue = actionValue
    pass

class Assertions:
    def __init__(self, assertion_type, assertion_action, assertion_value):
        self.assertion_type = assertion_type
        self.assertion_action = assertion_action
        self.assertion_value = assertion_value
    pass