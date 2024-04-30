import javalang
import javalang.tokenizer
from TestObjects import *

def tokenize_java_file(file_name):
    alltokens = []
    with open(file_name, 'r') as file:
        for line in file:
            if not line.strip().startswith('/*'):
                tokens = list(javalang.tokenizer.tokenize(line))
                alltokens.extend(tokens)
    return alltokens

def extract_test_cases(alltokens):
    alltestTokens = []
    flag = False 
    for i in range (len(alltokens)):
        if alltokens[i].value == "@" and alltokens[i+1].value == "Test":
            flag = True
        if alltokens[i].value == "}" and flag:
            alltestTokens.append(alltokens[i])
            flag = False
        if flag == True:
            alltestTokens.append(alltokens[i])
    return alltestTokens

def getTestCaseNames(testTokens):
    testCaseObjects = [] # array of all the test cases in the Appium file
    for i in range(len(testTokens)):
        if testTokens[i].value == "public" and testTokens[i+1].value == "void":
            test_case = TestCase(testTokens[i+2].value, [], [], [], [])
            testCaseObjects.append(test_case)
    return testCaseObjects

def ajdecoder(allTestTokens, testCaseObjects):
    #Keywords
    variableIdentifierKeywords = {'int', 'double', 'float', 'boolean', 'char', 'byte', 'short', 'long', 'WebElement', 'val'}
    assertionKeywords = {'Assert', 'assert'}
    assertionTypeKeywords = {'assertEquals', 'assertTrue', 'assertFalse', 'assertNull', 'assertNotNull'}
    assertionActionKeywords = {'getText', 'getAttribute', 'isEnabled', 'isSelected', 'isDisplayed', 'getSize', 'getLocation', 'getTagName', 'getCssValue'}
    variablePathIdentifierKeywords = {'xpath', 'id'}
    actionKeywords = {'sendKeys', 'click'}
    for test_case in testCaseObjects:
        testTokens = []
        startIndex = None
        endIndex = None
        
        structure = []
        variableNames = []
        actionNames = []
        assertionNames = []
        assertFlag = False
        
        variableIdType=[]
        variableIds=[]
        
        actionActions = []
        actionValues = []
        
        assertionTypes = []
        assertionActions = []
        assertionValues = []
        
        
        #------------------------------------------
        #This section extracts the test case tokens
        '''
        for token in allTestTokens:
            print(token.value)
        '''
        
        for i, token in enumerate(allTestTokens):
            if token.value == test_case.name:
                startIndex = i
            elif token.value == "}" and startIndex is not None and endIndex is None:
                endIndex = i

        # Extract the tokens for the test case method
        if startIndex is not None and endIndex is not None:
            testTokens= allTestTokens[startIndex:endIndex + 1]
            
        #------------------------------------------
        #This section extracts the names of the variables, actions and assertions
        for i, token in enumerate(testTokens):
            #print("Token:", token.value)
            if token.value in assertionKeywords:
                assertFlag = True
                #print("Assert Flag:", assertFlag)
            if token.value in variableNames and not assertFlag:
                actionNames.append(token.value)
                structure.append("AV" + str(len(actionNames)-1))
                #print("Action Names:", actionNames, "Structure:", structure)
            elif token.value in variableNames and assertFlag:
                assertionNames.append(token.value)
                structure.append("A" + str(len(assertionNames)-1))
                #print("Assertion Names:", assertionNames, "Structure:", structure)
                assertFlag = False
            if token.value.isidentifier() and testTokens[i-1].value in variableIdentifierKeywords:
                variableNames.append(token.value)
                structure.append("V" + str(len(variableNames)-1))
                #print("Variable Names:", variableNames, "Structure:", structure)
        #print("Variable Names:", variableNames)
        #print("Action Names:", actionNames)
        #print("Assertion Names:", assertionNames)
        #print("Structure:", structure, "\n")
        
        #------------------------------------------
        #This section extracts the ids of the variables
        for i, token in enumerate(testTokens):
            if token.value in variableNames:
                actualPath = ""
                while testTokens[i].value != ";":
                    if testTokens[i].value in variablePathIdentifierKeywords and testTokens[i+1].value == "(":
                        pathId = testTokens[i+2].value
                        if testTokens[i].value == "xpath":
                            variableIdType.append("xpath")
                            variableIds.append(pathId[1:-1])
                            break
                        else:
                            variableIdType.append("id")
                            for k in range(len(pathId)):
                                if pathId[k] == "/":
                                    while pathId[k] != "\"":
                                        actualPath += pathId[k]
                                        k+=1
                            variableIds.append(actualPath[1:])
                            break
                    i+=1
        #print("Variable Ids:", variableIds)
        
        #------------------------------------------
        #This section extracts the actions and action values for the variables
        for i, token in enumerate(testTokens):
            if token.value in actionNames:
                if testTokens[i+1].value == "." and testTokens[i+2].value in actionKeywords:
                    actionActions.append(testTokens[i+2].value)
                    if testTokens[i+2].value == "click":
                        actionValues.append(" ")
                    else:
                        actionValues.append(testTokens[i+4].value[1:-1])
        #print("Action Names:", actionNames)
        #print("Action Actions:", actionActions)
        #print("Action Values:", actionValues)
        
        #------------------------------------------
        #This section extracts the assertions and assertion values for the variables
        for i, token in enumerate(testTokens):
            if token.value in assertionKeywords:
                #print("Token:", token.value)
                if testTokens[i+1].value == "." and testTokens[i+2].value in assertionTypeKeywords:
                    assertionTypes.append(testTokens[i+2].value)
                while testTokens[i].value != ";":
                    if testTokens[i].value in assertionNames:
                        if testTokens[i+1].value == "." and testTokens[i+2].value in assertionActionKeywords:
                            assertionActions.append(testTokens[i+2].value)
                            assertionValues.append(testTokens[i+6].value[1:-1])
                    i+=1
        #print("Assertion Names:", assertionNames)
        #print("Assertion Types:", assertionTypes)
        #print("Assertion Actions:", assertionActions)
        #print("Assertion Values:", assertionValues)
        #print("\n")
        
        #------------------------------------------
        #This section creates the objects
        
        ''' Pre-Object Debugging Print Statements
        print("Test Case Name:", test_case.name)
        print("Structure:", structure)
        print("Variable Names:", variableNames, len(variableNames))
        print("Variable Id Type:", variableIdType, len(variableIdType))
        print("Variable Ids:", variableIds, len(variableIds))
        print("Action Names:", actionNames, len(actionNames))
        print("Action Actions:", actionActions, len(actionActions))
        print("Action Values:", actionValues, len(actionValues))
        print("Assertion Names:", assertionNames, len(assertionNames))
        print("Assertion Types:", assertionTypes, len(assertionTypes))
        print("Assertion Actions:", assertionActions, len(assertionActions))
        print("Assertion Values:", assertionValues, len(assertionValues))
        print("\n")
        '''
        
        for i in range(len(variableNames)):
            variable = Variable(variableNames[i], variableIdType[i], variableIds[i])
            test_case.variables.append(variable)  
        for i in range(len(actionNames)):
            action = Action(actionNames[i], actionActions[i], actionValues[i])
            test_case.actions.append(action)
        for i in range(len(assertionNames)):
            assertion = Assertion(assertionNames[i], assertionTypes[i], assertionActions[i], assertionValues[i])
            test_case.assertions.append(assertion)
        test_case.structure = structure
        
        ''' Object Debugging Print Statements
        for test_case in testCaseObjects:
            print("Test Case Name:", test_case.name)
            print("Structure:", test_case.structure)
            print("Variables:")
            for variable in test_case.variables:
                print(variable.name, variable.vId)
            print("Actions:")
            for action in test_case.actions:
                print(action.name, action.action, action.actionValue)
            print("Assertions:")
            for assertion in test_case.assertions:
                print(assertion.name, assertion.assertion_type, assertion.assertion_action, assertion.assertion_value)
            print("\n")
        '''
        #------------------------------------------
        #This section clears out all variables, ready for the next test case
        testTokens = []
        startIndex = None
        endIndex = None
        
        structure = []
        variableNames = []
        actionNames = []
        assertionNames = []
        assertFlag = False
        
        variableIds=[]
        
        actionActions = []
        actionValues = []
        
        assertionTypes = []
        assertionActions = []
        assertionValues = []
        
    return testCaseObjects
