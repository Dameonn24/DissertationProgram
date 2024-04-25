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
            test_case = TestCase(testTokens[i+2].value, [], [], [], [])
            testCaseObjects.append(test_case)
    return testCaseObjects

def ajdecoder(testTokens, testCaseObjects):
    variableIdentifierKeywords = {'int', 'double', 'float', 'boolean', 'char', 'byte', 'short', 'long', 'WebElement', 'val'}
    variablePathIdentifierKeywords = {'xpath', 'id'}
    actionKeywords = {'sendKeys', 'click'}
    listTokens = []
    currindex = 0
    
    currentVariableNames = []
    currentVariableIdType=[]
    currentVariableIds=[]
    
    currentActionVariableNames = []
    currentActionVariableActions=[]
    currentActionVariableValues=[]
    
    currentAssertionNames=[]
    currentAssertionType=[]
    currentAssertionValue=[]
    currentAssertionAction=[]
    assertFlag=False
    idOffset = 0
    
    structure=[]
    
    
    for test_case in testCaseObjects:
        for j in range(len(testTokens)):
            if testTokens[j].value == test_case.name:
                for i in range(j, len(testTokens)):
                    
                    #------------------------------------------
                    # This section enters all the variable information into the current test case object and reset for the next test case
                    if (testTokens[i].value == ";" and i == len(testTokens) - 1) or (testTokens[i].value == ";" and testTokens[i+1].value == "@"):    
                        
                        
                        #Testing output statements
                        print("currentVariableNames:", currentVariableNames, len(currentVariableNames))
                        print("Id Type:", currentVariableIdType, len(currentVariableIdType))
                        print("Ids:", currentVariableIds, len(currentVariableIds))
                        print("currentActionVariableNames:", currentActionVariableNames, len(currentActionVariableNames))
                        print("currentActionVariableActions:", currentActionVariableActions, len(currentActionVariableActions))
                        print("currentActionVariableValues:", currentActionVariableValues, len(currentActionVariableValues))
                        print("currentAssertionNames:", currentAssertionNames, len(currentAssertionNames))
                        print("currentAssertionType:", currentAssertionType, len(currentAssertionType))
                        print("currentAssertionAction:", currentAssertionAction, len(currentAssertionAction))
                        print("currentAssertionValue:", currentAssertionValue, len(currentAssertionValue))
                        print("structure:", structure, len(structure))
                        print("\n")
                        
                        
                        #------------------------------------------
                        #Creating the objects
                        
                        test_case.structure = structure
                        
                        for test_case in testCaseObjects:
                            for i in range(len(currentVariableNames)):
                                variable = Variable(currentVariableNames[i], currentVariableIdType[i], currentVariableIds[i])
                                test_case.variables.append(variable)
                            for i in range(len(currentActionVariableNames)):
                                action = Action(currentActionVariableNames[i], currentActionVariableActions[i], currentActionVariableValues[i])
                                test_case.actions.append(action)
                            for i in range(len(currentAssertionNames)):
                                assertion = Assertion(currentAssertionNames[i], currentAssertionType[i], currentAssertionAction[i], currentAssertionValue[i])
                                test_case.assertions.append(assertion)
                            
                            #Printing the test case objects
                            print(test_case.name, ":")
                            print("Structure:", test_case.structure)
                            print("Variables:")
                            for variable in test_case.variables:
                                print(variable.name, variable.vIdType, variable.vId)
                            print("\n")
                            print("Actions:")
                            for action in test_case.actions:
                                print(action.name, action.action, action.actionValue)
                            print("\n")
                            print("Assertions:")
                            for assertion in test_case.assertions:
                                print(assertion.name, assertion.assertion_type, assertion.assertion_action, assertion.assertion_value)
                            print("\n")  
                            
                                
                        currentVariableNames = []
                        currentVariableIdType=[]
                        currentVariableIds=[]
                        
                        currentActionVariableNames = []
                        currentActionVariableActions=[]
                        currentActionVariableValues=[]
                        
                        currentAssertionNames=[]
                        currentAssertionType=[]
                        currentAssertionValue=[]
                        currentAssertionAction=[]
                        assertFlag=False
                        idOffset = 0
                         
                        structure=[]
                        
                        
                        break
                    
                    #------------------------------------------
                    # This section extracts the variable names
                    
                    assertionTypes = {'assertEquals', 'assertTrue', 'assertFalse', 'assertNull', 'assertNotNull'}
                    listTokens.append(testTokens[i].value)
                    if (testTokens[i].value == "Assert"):
                            assertFlag=True
                            if testTokens[i+2].value in assertionTypes:
                                currentAssertionType.append(testTokens[i+2].value)
                                currentAssertionNames.append(testTokens[i+4].value)
                                currentAssertionAction.append(testTokens[i+6].value)
                                value=testTokens[i+10].value
                                currentAssertionValue.append(value[1:-1])
                                structure.append("A" + str(len(currentAssertionNames)-1)+testTokens[i+4].value)
                    elif (testTokens[i].value in currentVariableNames and not assertFlag): #incase there are variables that perform multiple actions #assertFlag is used to filter out the assertion names
                            currentActionVariableNames.append(testTokens[i].value)
                            currindex=currentActionVariableNames.index(testTokens[i].value)
                            structure.append("AV" + str(len(currentActionVariableNames)-1)+testTokens[i].value)
                    elif (testTokens[i].value in variableIdentifierKeywords and testTokens[i+1].value.isidentifier()):
                        currentVariableNames.append(testTokens[i+1].value)
                        structure.append("V" + str(len(currentVariableNames)-1)+testTokens[i+1].value)
                    
                    #------------------------------------------
                    # This section extracts the variable ids
                    if testTokens[i].value in currentVariableNames:
                        actualPath = ""
                        while testTokens[i].value != ";":
                            if testTokens[i].value in variablePathIdentifierKeywords and testTokens[i+1].value == "(":
                                pathId = testTokens[i+2].value
                                if testTokens[i].value == "xpath":
                                    currentVariableIdType.append(testTokens[i].value)
                                    currentVariableIds.append(pathId[1:-1])
                                    break
                                else:
                                    currentVariableIdType.append(testTokens[i].value)
                                    for k in range(len(pathId)):
                                        if pathId[k] == "/":
                                            while pathId[k] != "\"":
                                                actualPath += pathId[k]
                                                k+=1
                                    currentVariableIds.append(actualPath[1:])
                                    break
                            i+=1
                    
                    #------------------------------------------
                    #This sections extract the actions and action values for the variables
                    i=i-1
                    if testTokens[i].value in currentActionVariableNames:
                        while testTokens[i].value != ";":
                            if testTokens[i].value in actionKeywords:
                                currentActionVariableActions.append(testTokens[i].value)
                                if testTokens[i].value == "click":
                                    currentActionVariableValues.append(" ")
                                else:
                                    currActionValue = testTokens[i+2].value
                                    currentActionVariableValues.append(currActionValue[1:-1])
                            i+=1     
                    
                    #------------------------------------------
                    #This section filter out the assertion names
                    '''
                    assertionKeywords = {'Assert', 'assert'}
                    
                    if testTokens[i].value in assertionKeywords:
                        while testTokens[i].value != ";":
                            if testTokens[i].value in assertionTypes:
                                currentAssertionType.append(testTokens[i].value)
                            for vname in currentActionVariableNames:
                                if testTokens[i].value == vname:
                                    currentAssertionNames.append(vname)
                                    print("currentAssertionNames:", currentAssertionNames)
                                    replaceIndex = currentActionVariableNames.index(vname)
                                    print("vname:",vname,"replaceIndex:", replaceIndex)
                                    currindex=currentAssertionNames.index(vname)
                                    print("currindex:", currindex)
                                    print("before structure:", structure)
                                    replaceStructureIndex = structure.index("AV" + str(replaceIndex+idOffset)+vname)
                                    structure[replaceStructureIndex]="A" + str(currindex) 
                                    print("after structure:", structure)
                                    print("before currentActionVariableNames:", currentActionVariableNames)
                                    currentActionVariableNames.remove(currentActionVariableNames[replaceIndex])
                                    print("after currentActionVariableNames:", currentActionVariableNames, "\n")
                                    idOffset +=1
                                    if testTokens[i+1].value == ".":
                                        currentAssertionAction.append(testTokens[i+2].value)
                                        value=testTokens[i+6].value
                                        currentAssertionValue.append(value[1:-1])
                            i += 1
                    '''
                    #------------------------------------------
                    
                    
                
    return testCaseObjects




# Example usage
'''
file_name = "appiumTests/AppiumTrialLevel3.java"
alltokens = tokenize_java_file(file_name)
testTokens = extract_test_cases(alltokens)
testCaseObjects = getTestCaseNames(testTokens)
ajd = getVariablesAndAssertions(testTokens, testCaseObjects) #ajd = appium java decoder

for test_case in testCaseObjects:
    
    print("Test Name:", test_case.name)
    print("Structure:", test_case.structure)
    print("Variable Names:", test_case.variables)
    #print("Variable Ids:", test_case.variableIds)
    #print("Assertions:", test_case.assertions)
    #print("Actions:", test_case.actions)
    print("\n")
'''