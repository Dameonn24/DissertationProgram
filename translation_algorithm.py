import javalang
import javalang.tokenizer

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
testCounter = 0
for i in range (len(alltokens)):
    if alltokens[i].value == "@" and alltokens[i+1].value == "Test":
        flag = True
        testCounter += 1 #counts how many test cases are there in the file
    if alltokens[i].value == "}":
        flag = False
    if flag == True:
        testTokens.append(alltokens[i])

testNames = [] #Store the name of the test case
variableNames = [] #store the variables used
variableActions = [] #store the actions performed by the variables

#isolate the names of the test cases
def getTestCasesName(testTokens, testCounter):
    testName = [''] * testCounter
    i = 0
    for j in range(len(testTokens)):
        if testTokens[j].value == "public" and testTokens[j+1].value == "void":
            testNames[i] = testTokens[j+2].value
            i += 1

    return testNames

#isolate the name of the variables
def getVariableName(testTokens):
    keywords = {'int', 'double', 'float', 'boolean', 'char', 'byte', 'short', 'long', 'WebElement', 'val'}
    variableNames = []
    for i in range(len(testTokens)):
        if testTokens[i].value in keywords and testTokens[i+1].value.isidentifier():
            variableNames.append(testTokens[i+1].value)
        if (testTokens[i].value == ";" and i == len(testTokens) - 1) or (testTokens[i].value == ";" and testTokens[i+1].value == "@"):
            variableNames.append("XXX") #seperates the variable names in different test cases
    return variableNames

#ioslate the xpath / id to the variable names
def getVariableId(testTokens):
    #variableIDKeywords = {'id', 'xpath'}
    appiumVariableLocatorsJargon = {'By', 'AppiumBy'}
    variableIds = []
    flag = False
    fullIdToken = ""
    for i in range (len(testTokens)):
        if testTokens[i].value in appiumVariableLocatorsJargon and testTokens[i+1].value == ".":
            flag = True
        if flag == True:
            fullIdToken = fullIdToken + testTokens[i].value
        if testTokens[i].value == ")" and flag == True:
            variableIds.append(fullIdToken)
            flag = False
            fullIdToken = ""
        if (testTokens[i].value == ";" and i == len(testTokens) - 1) or (testTokens[i].value == ";" and testTokens[i+1].value == "@"):
            variableIds.append("XXX") 
            
    return variableIds

#isolate the actions performed by the variables
def getVariableActions(testTokens):
    keywords = {'sendKeys', 'click'} #add other outputs
    actions = []
    flag = False
    action = ""
    for i in range(len(testTokens)):
        if testTokens[i].value == "."  and testTokens[i+1].value in keywords:
            if testTokens[i+1].value == "click":
                action = "click()"
                actions.append(action)
                action = ""
            if testTokens[i+1].value == "sendKeys":
                flag = True
        if flag == True:
            action = action + testTokens[i].value
        if testTokens[i].value == ")" and flag == True:
            action = action[1:]
            actions.append(action)
            action = ""
            flag = False
        if (testTokens[i].value == ";" and i == len(testTokens) - 1) or (testTokens[i].value == ";" and testTokens[i+1].value == "@"):
            actions.append("XXX")
    return actions

#isolate assertions
def getAssertions(testTokens,variableNames):
    assertions = []
    flag = False
    assertToken = ""
    keywords = {'Assert', 'assert'}
    for i in range (len(testTokens)):
        if testTokens[i].value in keywords:
             flag = True
             #print(testTokens[i].value)
             while testTokens[i].value not in variableNames:
                 #print(testTokens[i].value)
                 i += 1
        if flag == True:
            #print("current token: ", testTokens[i].value)
            #print ("current assertToken before: ", assertToken)
            assertToken = assertToken + testTokens[i].value
            #print ("current assertToken after: ", assertToken)
        if testTokens[i].value == ")" and testTokens[i+1].value == ";" and flag == True:
            assertions.append(assertToken)
            flag = False
            assertToken = ""
        if (testTokens[i].value == ";" and i == len(testTokens) - 1) or (testTokens[i].value == ";" and testTokens[i+1].value == "@"):
            assertions.append("XXX")
    return assertions

'''
assertionType = []
assertionVariableName = []
assertionAction = []
assertionValue = []
def getAssertionsTwo(testTokens, variableNames):
    keywords = {'Assert','assert'}
    assertionFlag = False
    assertionValueFlag = False
    currentAssertionValue = ""
    for i in range (len(testTokens)):
        currentToken = testTokens[i].value
        if currentToken in keywords:
            assertionFlag = True
            if currentToken == "." and assertionFlag == True:
                assertionType.append(testTokens[i+1])
        if currentToken in variableNames and assertionFlag == True:
            assertionVariableName.append(currentToken)
            if assertionVariableName and currentToken == "." and assertionFlag == True:
                assertionAction.append (testTokens[i+1])
        if currentToken == '"' and assertionFlag == True:
            assertionValueFlag = True
        if assertionValueFlag == True and assertionFlag == True:
            currentAssertionValue = currentAssertionValue + currentToken
        if currentToken == '"' and assertionFlag == True and assertionValueFlag == True:
            assertionValue.append(currentAssertionValue)
            currentAssertionValue = ""
            assertionValueFlag = False
        if (testTokens[i].value == ";" and i == len(testTokens) - 1) or (testTokens[i].value == ";" and testTokens[i+1].value == "@"):
            assertionType.append("XXX")
            assertionVariableName.append("XXX")
            assertionAction.append("XXX")
            assertionValue.append("XXX")
    return assertionType, assertionVariableName, assertionAction, assertionValue
'''

#TESTING
#print(getVariableActions(testTokens))
#print(getVariableId(testTokens))
#print(getVariableName(testTokens))
#print(getTestCasesName(testTokens,testCounter))
variableNames = getVariableName(testTokens)
print(getAssertions(testTokens, variableNames))