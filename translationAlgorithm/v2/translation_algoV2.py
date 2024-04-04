import javalang
import javalang.tokenizer
from TestCase import TestCase, Variable, InitialisedVariable, Assertions

def tokenize_java_file(file_name):
    alltokens = []
    with open(file_name, 'r') as file:
        for line in file:
            if not line.strip().startswith('/*'):
                tokens = list(javalang.tokenizer.tokenize(line))
                alltokens.extend(tokens)
    return alltokens

def extract_test_cases(alltokens):
    testTokens = []
    flag = False 
    for i in range (len(alltokens)):
        if alltokens[i].value == "@" and alltokens[i+1].value == "Test":
            flag = True
        if alltokens[i].value == "}":
            flag = False
        if flag == True:
            testTokens.append(alltokens[i])
    return testTokens

def getTestCaseNames(testTokens):
    testCaseObjects = [] # array of all the test cases in the Appium file
    for i in range(len(testTokens)):
        if testTokens[i].value == "public" and testTokens[i+1].value == "void":
            test_case = TestCase(testTokens[i+2].value,[""])
            testCaseObjects.append(test_case)
    return testCaseObjects

def getVariables(testTokens, testCaseObjects):
    variableIdentifierKeywords = {'int', 'double', 'float', 'boolean', 'char', 'byte', 'short', 'long', 'WebElement', 'val'}
    variablePathIdentifierKeywords = {'xpath', 'id'}
    
    mainVariableArray = []
    currentVariableNames = []
    currentInitialisedVariableNames = []
    structure=[]
    
    #currentVariableIds = []
    #currentVariableActions = []
    #currentVariableActionValues = []
    
    for test_case in testCaseObjects:
        for j in range(len(testTokens)):
            if testTokens[j].value == test_case.name:
                for i in range(j, len(testTokens)):
                    
                    # This section enters all the variable information into the current test case object and reset for the next test case
                    if (testTokens[i].value == ";" and i == len(testTokens) - 1) or (testTokens[i].value == ";" and testTokens[i+1].value == "@"):
                        for b in range(len(mainVariableArray)):
                            if mainVariableArray[b] in currentVariableNames:
                                currentInitialisedVariableNames.append(mainVariableArray[b])
                                currentIndex= "I" + str(b)
                                structure.append(currentIndex)
                            else:
                                currentVariableNames.append(mainVariableArray[b])
                                currentIndex= "V" + str(b)
                                structure.append(currentIndex)
                        '''
                        print("\n mainVariableArray:", mainVariableArray, len(mainVariableArray))
                        print("currentVariableNames:", currentVariableNames, len(currentVariableNames))
                        print("currentInitialisedVariableNames:", currentInitialisedVariableNames, len(currentInitialisedVariableNames))
                        print("structure:", structure, len(structure))
                        '''
                        test_case.structure = structure
                        
                        mainVariableArray = []
                        currentVariableNames = []
                        currentInitialisedVariableNames = []
                        structure=[]
                        break
                    
                    # This section extracts the variable names
                    if (testTokens[i].value in variableIdentifierKeywords and testTokens[i+1].value.isidentifier()):
                        mainVariableArray.append(testTokens[i+1].value)
                    elif (testTokens[i].value in mainVariableArray): #incase there are variables that perform multiple actions
                        mainVariableArray.append(testTokens[i].value)
                        #print(mainVariableArray)
                    for a in range(len(mainVariableArray)-2): #This loop is to filters out any unnecessary duplicates
                        if (mainVariableArray[a] == mainVariableArray[a+1]) and (mainVariableArray[a]== mainVariableArray[a+2]):
                            mainVariableArray=mainVariableArray[:a]+mainVariableArray[a+2:]
                    
                    # This section extracts the variable ids
                    if testTokens[i].value in currentVariableNames:
                        
                    
                    
                    
    return testCaseObjects




# Example usage
file_name = "appiumTests/AppiumTrialLevel3.java"
alltokens = tokenize_java_file(file_name)
testTokens = extract_test_cases(alltokens)
testCaseObjects = getTestCaseNames(testTokens)
variables = getVariables(testTokens, testCaseObjects)

for test_case in testCaseObjects:
    print("Test Name:", test_case.name)
    print("Structure:", test_case.structure)
'''
    print("Variable Names:", test_case.variables)
    #print("Variable Ids:", test_case.variableIds)
    #print("Assertions:", test_case.assertions)
    #print("Actions:", test_case.actions)
    print("\n")
'''