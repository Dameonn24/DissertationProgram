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

testName = [] #Store the name of the test case
variableNames = [] #store the variables used
variableActions = [] #store the actions performed by the variables

#isolate the names of the test cases
def getTestCasesName(testTokens, testCounter):
    testName = [''] * testCounter
    i = 0
    for j in range(len(testTokens)):
        if testTokens[j].value == "public" and testTokens[j+1].value == "void":
            testName[i] = testTokens[j+2].value
            i += 1

    return testName
print(getTestCasesName(testTokens,testCounter))

#isolate the name of the variables
def getTestCaseVariables(testTokens):
    keywords = {'int', 'double', 'float', 'boolean', 'char', 'byte', 'short', 'long', 'WebElement', 'val'}
    variableNames = []
    for i in range(len(testTokens)):
        print (testTokens[i].value)
        if testTokens[i].value in keywords and testTokens[i+1].value.isidentifier():
            variableNames.append(testTokens[i+1].value)
        if (testTokens[i].value == ";" and i == len(testTokens) - 1) or (testTokens[i].value == ";" and testTokens[i+1].value == "@"):
            variableNames.append("XXX") #seperates the variable names in different test cases
    return variableNames
print(getTestCaseVariables(testTokens))

#ioslate the xpath / id to the variable names
def getVariableId(testTokens):
    variableIDKeywords = {'id', 'xpath'}
    appiumVariableLocatorsJargon = {'By', 'AppiumBy'}
    variableIds = []
    flag = False
    fullToken = ""
    for i in range (len(testTokens)):
        if testTokens[i].value in appiumVariableLocatorsJargon and testTokens[i+1].value == ".":
            flag = True
        if flag == True:
            #if testTokens[i] in variableIDKeywords
            fullToken = fullToken + testTokens[i].value
        if testTokens[i].value == "}":
            flag = False
            variableIds.append(fullToken)
    return variableIds

print(getVariableId(testTokens))


#isolate the actions performed by the variables
def getVariableActions(testTokens):
    keywords = {'sendKeys', 'click'} #add other outputs
    actions = []
    for i in range(len(testTokens)):
        if testTokens[i].value == "."  and testTokens[i+1].value in keywords:
            actions.append(testTokens[i+1].value)
        if (testTokens[i].value == ";" and i == len(testTokens) - 1) or (testTokens[i].value == ";" and testTokens[i+1].value == "@"):
            actions.append("XXX")
    return actions

#isolate assertions


print(getVariableActions(testTokens))

