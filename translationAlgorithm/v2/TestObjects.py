#APPIUM JAVA DECODER OBJECTS
class TestFile:
    def __init__(self, name, package, testCases):
        self.name = name
        self.package = package
        self.testCases = testCases
    pass
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
