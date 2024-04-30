#APPIUM JAVA DECODER OBJECTS
class TestCase:
    def __init__(self, name, structure , variables, actions, assertions):
        self.name = name
        self.structure = structure
        self.variables = variables
        self.actions = actions
        self.assertions = assertions
    pass

class Variable:
    def __init__(self, name, vIdType, vId):
        self.name = name
        self.vIdType = vIdType
        self.vId = vId
    pass

class Action:
    def __init__(self, name, action, actionValue):
        self.name = name
        self.action = action
        self.actionValue = actionValue
    pass

class Assertion:
    def __init__(self, name, assertionType, assertionAction, assertionValue):
        self.name = name
        self.assertionType = assertionType
        self.assertionAction = assertionAction
        self.assertionValue = assertionValue
    pass

#TRANSLATION ALGORITHM OBJECTS
class TranslatedTestCase:
    def __init__(self, name, structure, tVariables, tActions, tAssertions):
        self.name = name
        self.structure = structure
        self.tVariables = tVariables
        self.tActions = tActions
        self.tAssertions = tAssertions
    pass

class TranslatedVariables:
    def __init__(self, name, vId):
        self.name = name
        self.vId = vId
    pass

class TranslatedActions:
    def __init__(self, name, action):
        self.name = name
        self.action = action
    pass

class TranslatedAssertions:
    def __init__(self, name, assertion):
        self.name = name
        self.assertion = assertion
    pass