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
            test_case = TestCase(testTokens[i+2].value,[""])
            testCaseObjects.append(test_case)
    return testCaseObjects

def ajdecoder(testTokens, testCaseObjects):
    variableIdentifierKeywords = {'int', 'double', 'float', 'boolean', 'char', 'byte', 'short', 'long', 'WebElement', 'val'}
    variablePathIdentifierKeywords = {'xpath', 'id'}
    actionKeywords = {'sendKeys', 'click'}
    
    currindex = 0
    mainVariableArray = []
    
    currentVariableNames = []
    currentVariableIds=[]
    
    currentActionVariableNames = []
    currentActionVariableActions=[]
    currentActionVariableValues=[]
    
    currentAssertionNames=[]
    currentAssertionType=[]
    currentAssertionValue=[]
    currentAssertionAction=[]
    
    structure=[]
    
    
    for test_case in testCaseObjects:
        for j in range(len(testTokens)):
            if testTokens[j].value == test_case.name:
                for i in range(j, len(testTokens)):
                    
                    #------------------------------------------
                    # This section enters all the variable information into the current test case object and reset for the next test case
                    if (testTokens[i].value == ";" and i == len(testTokens) - 1) or (testTokens[i].value == ";" and testTokens[i+1].value == "@"):
                        
                        '''
                        # This section filters out any unnecessary duplicates -- primarily formatting
                        for a in range(len(mainVariableArray)-2): 
                            if (a+2 < len(mainVariableArray)) and (mainVariableArray[a] == mainVariableArray[a+1]) and (mainVariableArray[a] == mainVariableArray[a+2]):
                                mainVariableArray=mainVariableArray[:a]+mainVariableArray[a+2:]
                        for a in range(len(mainVariableArray)-1):
                            if "A*" in mainVariableArray[a] and "A*" in mainVariableArray[a+1]:
                                mainVariableArray=mainVariableArray[:a]+mainVariableArray[a+1:]
                        
                        
                        # This section distributes the variables into their respective categories and extracts a structure
                        # This section splits between variables and initialised variables
                        for b in range(len(currentActionVariableNames)):
                            if mainVariableArray[b] in currentVariableNames:
                                currentInitialisedVariableNames.append(mainVariableArray[b])
                                currentIndex= "I" + str(currentInitialisedVariableNames.index(mainVariableArray[b]))
                                structure.append(currentIndex)
                            else:
                                currentVariableNames.append(mainVariableArray[b])
                                currentIndex= "V" + str(currentVariableNames.index(mainVariableArray[b]))
                                structure.append(currentIndex)
                        
                        # This section splits between variables and assertions
                        for c in range(len(currentVariableNames)):
                            if "A*" in currentVariableNames[c]:
                                d = mainVariableArray.index(currentVariableNames[c])
                                assertName = currentVariableNames[c].replace("A*", "")
                                currentAssertionNames.append(assertName)
                                currrentAssertionIds.append(ids[c])
                                currentVariableNames.remove(currentVariableNames[c])
                                ids.remove(ids[c])
                                structure[d] = "A" + str(currentAssertionNames.index(assertName))
                        '''
                                
                        #Testing output statements
                        #print("mainVariableArray:", mainVariableArray, len(mainVariableArray))
                        print("currentVariableNames:", currentVariableNames, len(currentVariableNames))
                        print("Ids:", currentVariableIds, len(currentVariableIds))
                        print("currentActionVariableNames:", currentActionVariableNames, len(currentActionVariableNames))
                        print("currentActionVariableActions:", currentActionVariableActions, len(currentActionVariableActions))
                        print("currentActionVariableValues:", currentActionVariableValues, len(currentActionVariableValues))
                        print("currentAssertionNames:", currentAssertionNames, len(currentAssertionNames))
                        #print("currentAssertionIds:", currrentAssertionIds, len(currrentAssertionIds))
                        print("currentAssertionType:", currentAssertionType, len(currentAssertionType))
                        print("currentAssertionAction:", currentAssertionAction, len(currentAssertionAction))
                        print("currentAssertionValue:", currentAssertionValue, len(currentAssertionValue))
                        print("structure:", structure, len(structure))
                        print("\n")
                        
                        test_case.structure = structure
                        
                        #TODO: Create the variable objects and add them to the test case object
                        
                        mainVariableArray = []
    
                        currentVariableNames = []
                        currentVariableIds=[]
                        
                        currentActionVariableNames = []
                        currentActionVariableActions=[]
                        currentActionVariableValues=[]
                        
                        currentAssertionNames=[]
                        currentAssertionType=[]
                        currentAssertionValue=[]
                        currentAssertionAction=[]
                        
                        structure=[]
                        
                        
                        break
                    
                    #------------------------------------------
                    # This section extracts the variable names
                    if (testTokens[i].value in variableIdentifierKeywords and testTokens[i+1].value.isidentifier()):
                        currentVariableNames.append(testTokens[i+1].value)
                        currindex=currentVariableNames.index(testTokens[i+1].value)
                        structure.append("V" + str(currindex))
                    elif (testTokens[i].value in currentVariableNames): #incase there are variables that perform multiple actions
                        currentActionVariableNames.append(testTokens[i].value)
                        currindex=currentActionVariableNames.index(testTokens[i].value)
                        structure.append("AV" + str(currindex))
                    #------------------------------------------
                    # This section extracts the variable ids
                    if testTokens[i].value in currentVariableNames:
                        actualPath = ""
                        while testTokens[i].value != ";":
                            if testTokens[i].value in variablePathIdentifierKeywords and testTokens[i+1].value == "(":
                                pathId = testTokens[i+2].value
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
                    assertionKeywords = {'Assert', 'assert'}
                    assertionTypes = {'assertEquals', 'assertTrue', 'assertFalse', 'assertNull', 'assertNotNull'}
                    if testTokens[i].value in assertionKeywords:
                        while testTokens[i].value != ";":
                            if testTokens[i].value in assertionTypes:
                                #print("before currentAssertionType: ", currentAssertionType)
                                currentAssertionType.append(testTokens[i].value)
                                #print("after currentAssertionType: ",currentAssertionType)
                            for vname in currentActionVariableNames:
                                if testTokens[i].value == vname:
                                    currentAssertionNames.append(vname)
                                    currentActionVariableNames.remove(currentActionVariableNames[currentActionVariableNames.index(vname)])
                                    currindex=currentAssertionNames.index(vname)
                                    structure.append("A" + str(currindex))
                                    #print(testTokens[i-1].value, testTokens[i].value, testTokens[i+1].value)
                                    if testTokens[i+1].value == ".":
                                        #print("-- loop entered -- \n")
                                        #print("before currentAssertionAction: ", currentAssertionAction)
                                        #print("before currentAssertionValue: ", currentAssertionValue)
                                        currentAssertionAction.append(testTokens[i+2].value)
                                        value=testTokens[i+6].value
                                        currentAssertionValue.append(value[1:-1])
                                        #print("after currentAssertionAction: ", currentAssertionAction)
                                        #print("after currentAssertionValue: ", currentAssertionValue, "\n")
                            
                            '''            
                            for e in range(len(currentAssertionAction)-1):
                                if currentAssertionAction[e] == currentAssertionAction[e+1] and currentAssertionValue[e] == currentAssertionValue[e+1]:
                                    currentAssertionAction.remove(currentAssertionAction[e+1])
                                    currentAssertionValue.remove(currentAssertionValue[e+1])
                            '''
                            
                            i += 1
                    
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