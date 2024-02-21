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
    if alltokens[i].value == "}":
        flag = False
    if flag == True:
        testTokens.append(alltokens[i])

testNames = [] #Store the name of the test case
variableNames = [] #store the variables used
variableActions = [] #store the actions performed by the variables

#isolate the names of the test cases
def getTestCasesName(testTokens):
    testCasesName = []
    for i in range (len(testTokens)):
        if testTokens[i].value == "public" and testTokens[i+1].value == "void":
            testCasesName.append(testTokens[i+2].value)
    return testCasesName

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
#print(getTestCasesName(testTokens))
#variableNames = getVariableName(testTokens)
#print(getAssertions(testTokens, variableNames))


# ESPRESSO-KOTLIN ENCODER

# Convert the test tokens into Espresso-Kotlin code
espressoCode = """import androidx.test.espresso.Espresso.onView
import androidx.test.espresso.action.ViewActions.*
import androidx.test.espresso.assertion.ViewAssertions.*
import androidx.test.espresso.matcher.ViewMatchers.*
import androidx.test.ext.junit.rules.ActivityScenarioRule
import androidx.test.ext.junit.runners.AndroidJUnit4
import androidx.test.filters.LargeTest
import org.junit.Rule
import org.junit.Test
import org.junit.runner.RunWith

@LargeTest
@RunWith(AndroidJUnit4::class)
class EspressoTests {

    @Rule
    @JvmField
    var mActivityScenarioRule = ActivityScenarioRule(MainActivity::class.java) """

testNames = getTestCasesName(testTokens)
variableNames = getVariableName(testTokens)
variableActions = getVariableActions(testTokens)
variableIds = getVariableId(testTokens)

eof = False
i=0
j=0
while i < len(testNames):
    currentTestCase = "\n\n    @Test\n    fun " + testNames[i] + "(){\n"
    while j < len(variableNames):
        if variableNames[j] == "XXX":
            break
        currentTestCase = currentTestCase + "        val " + variableNames[j] + " = onView(withId(R.id."+ variableIds[j]+"))\n"+ "        " + variableNames[j]+variableActions[j] + "\n"
        j += 1
    espressoCode = espressoCode + currentTestCase
    i += 1
    j += 1


# Write the Espresso-Kotlin code to a file
outputFile = "test_espresso_code.kt"
with open(outputFile, 'w+') as file:
    file.writelines(espressoCode)

#print(espressoCode)

'''
# Write the Espresso-Kotlin code to a file
outputFile = "/u:/ManW10/Desktop/Dissertation/DissertationProgram/espresso_code.kt"
with open(outputFile, 'w') as file:
    file.write(espressoCode)
'''