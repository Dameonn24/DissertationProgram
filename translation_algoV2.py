import javalang
import javalang.tokenizer

# APPIUM-JAVA DECODER

#Convert the java file into a full list of tokens
alltokens=[]
file = "AppiumTrialLevel3.java"
with open(file, 'r') as file:
    for line in file:
        if not line.strip().startswith('/*'):
            tokens = list(javalang.tokenizer.tokenize(line))
            alltokens.extend(tokens)

# Isolate all the test cases from the appium test file.         
testTokens = [] #holds all the tests in the test case
flag = False 
for i in range (len(alltokens)):
    if alltokens[i].value == "@" and alltokens[i+1].value == "Test":
        flag = True
    if alltokens[i].value == "}" and flag:
        flag = False
        testTokens.append("END OF TEST CASE")
    if flag == True:
        testTokens.append(alltokens[i].value)

#print(testTokens)

class Test:
    def __init__(self, testName, variableNames, variableActions, variableActionValues, assertionType, assertVariable, assertToMessage):
        self.testName = testName
        self.variableNames = variableNames
        self.variableActions = variableActions
        self.variableActionValues = variableActionValues
        self.assertionType = assertionType
        self.assertVariable = assertVariable
        self.assertToMessage = assertToMessage
        

for test in tests:
    test = Test()


