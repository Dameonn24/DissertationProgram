class TestCase:
    def __init__(self, name):
        self.name = name
        self.variables = []
        self.assertions = []
        self.actions = []

    def add_variable(self, variablename):
        self.variables.append((variablename))

    def add_assertion(self, assertion_type, assertion_action, assertion_value):
        self.assertions.append((assertion_type, assertion_action, assertion_value))

    def add_action(self, action_name, action_value):
        self.actions.append((action_name, action_value))
