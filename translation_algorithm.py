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
            variableNames.append("ENDOFTESTCASE") #seperates the variable names in different test cases
    return variableNames

#ioslate the xpath / id to the variable names
def getVariableId(testTokens):
    variableIDKeywords = {'id', 'xpath'}
    #appiumVariableLocatorsJargon = {'By', 'AppiumBy'}
    variableIds = []
    fullIdToken = ""
    variableactualpath = ""
    for i in range (len(testTokens)):
        if testTokens[i].value == "id" and testTokens[i+1].value == "(":
            #print(testTokens[i+2])
            variablepath = testTokens[i+2].value
            #print(variablepath)
            flag = False
            for j in range (len(variablepath)):
                #print(variablepath[j])
                if variablepath[j] == "\"":
                    flag = False
                    variableIds.append(variableactualpath)
                    variableactualpath = ""
                if flag:
                    variableactualpath = variableactualpath + variablepath[j]
                if variablepath[j] == "/":
                    flag = True
        if (testTokens[i].value == ";" and i == len(testTokens) - 1) or (testTokens[i].value == ";" and testTokens[i+1].value == "@"):
            variableIds.append("ENDOFTESTCASE")
            flag = False       
    variableIds = [x for x in variableIds if x != '']
    return variableIds

#isolate the actions performed by the variables
def getVariableActions(testTokens):
    keywords = {'sendKeys', 'click'} #add other outputs
    assertKeywords = { 'Assert', 'assert'}
    actions = []
    actionsValue = []
    flag = False
    action = ""
    actionName = ""
    actionValue = ""
    for i in range(len(testTokens)):
        if testTokens[i].value in assertKeywords:
            actions.append("ASSERT")
            actionsValue.append("ASSERT")
        if testTokens[i].value == "."  and testTokens[i+1].value in keywords:
            if testTokens[i+1].value == "click":
                actions.append("click()")
                actionsValue.append("NOACTION")
            if testTokens[i+1].value == "sendKeys":
                flag = True
                actionName = "sendKeys()"
        if flag == True:
            action = action + testTokens[i].value
        if testTokens[i].value == ")" and flag == True:
            action = action[1:]
            newFlag = False
            for char in action: #this loop is to extract the action text that is being sent into the app
                if char == '(':
                    newFlag = True
                if newFlag and char == ')':
                    newFlag = False
                if newFlag:
                    actionValue += char
            actions.append(actionName)
            actionValue = actionValue[2:-1] #formatting to remove the ""
            actionsValue.append(actionValue)
            action = ""
            actionName = ""
            actionValue = ""
            flag = False
        if (testTokens[i].value == ";" and i == len(testTokens) - 1) or (testTokens[i].value == ";" and testTokens[i+1].value == "@"):
            actions.append("ENDOFTESTCASE")
            actionsValue.append("ENDOFTESTCASE")
    return actions, actionsValue

#isolate assertions
def getAssertions(testTokens,variableNames):
    keywords = {'Assert', 'assert'}
    assertionType = [] #assertEquals / assertTrue / assertFalse / assertNull
    assertionAction = [] # variableName.getText()
    assertionValue = [] # store the expected message
    
    for i in range(len(testTokens)):
        if testTokens[i].value in keywords:
            flag = True
        if flag and testTokens[i+1].value == ".": #condition to find the assertionType
            print(testTokens[i+2].value)
            assertionType.append(testTokens[i+2].value)
        while flag and testTokens[i].value not in variableNames:
            i+=1
        if flag and testTokens[i+1].value ==".":
            print(testTokens[i+2].value)
            assertion
            

#TESTING
#print(getVariableActions(testTokens))
#print(getVariableId(testTokens))
#print(getVariableName(testTokens))
#print(getTestCasesName(testTokens))
#variableNames = getVariableName(testTokens)
#print(getAssertions(testTokens, variableNames))


#TRANSLATION
def getKotlinTranslations(actions, actionsValue,assertion):
    translations = []
    for i in range(len(actions)):
        if actions[i] == "click()":
            translations.append("click()")
        if actions[i] == "sendKeys()":
            x = actionsValue[i]
            translations.append("replaceText(\""+x+"\"), closeSoftKeyboard()")
        if actions[i] == "ENDOFTESTCASE":
            translations.append("ENDOFTESTCASE")
    return translations 


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
variableActions, variableActionsValues = getVariableActions(testTokens)
variableIds = getVariableId(testTokens)
assertion = getAssertions(testTokens,variableNames)
variableTranslatedAction = getKotlinTranslations(variableActions,variableActionsValues,assertion)
print("Length of variableNames:", len(variableNames))
print("Length of variableTranslatedAction:", len(variableTranslatedAction))
print("content of variable names:", variableNames)
print("Contents of variableTranslatedAction:", variableTranslatedAction)

eof = False
i=0
i = 0
j = 0
for i in range(len(testNames)):
    currentTestCase = f"\n\n    @Test\n    fun {testNames[i]}(){{\n"
    while j < len(variableNames) and variableNames[j] != "ENDOFTESTCASE":
        print(j)
        currentTestCase += f"        val {variableNames[j]} = onView(withId(R.id.{variableIds[j]}))\n"
        currentTestCase += f"        {variableNames[j]}.perform({variableTranslatedAction[j]})\n"
        j += 1
    espressoCode += currentTestCase
    j += 1


# Write the Espresso-Kotlin code to a file
outputFile = "test_espresso_code.kt"
with open(outputFile, 'w+') as file:
    file.writelines(espressoCode)

