import javalang
import javalang.tokenizer
from TestObjects import *
from AJDecoder import *
from EKEncoder import *
import re

file_name = "testingMaterial/appiumTests/AppiumTrialLevel3.java" #CHANGE THE INPUT FILE HERE
alltokens = tokenize_java_file(file_name)
testTokens = extract_test_cases(alltokens)
testCaseObjects = getTestCaseNames(testTokens)
ajdTestCases = ajdecoder(testTokens, testCaseObjects) #ajd = appium java decoder

#-----------------------------
#TRANSLATION ALGORITHM
translatedTestCaseObjects = []

for testCase in ajdTestCases:
    translatedTestCase = TranslatedTestCase(testCase.name, testCase.structure, [], [], [])
    translatedTestCaseObjects.append(translatedTestCase)
    
    tNames = []
    tIds = []
    tActionNames = []
    tActionActions = []
    tAssertionNames = []
    tAssertionActions = []
    #print("Test Case Name:", testCase.name)
    
    #Translating Variables
    for variable in testCase.variables:
        #print("Variable Name:", variable.name)
        #print("Variable Type:", variable.vIdType)
        #print("Variable Id:", variable.vId)
        currentId = "findElement(Locator." + variable.vIdType.upper() + ", \"" + variable.vId + "\")"
        #print("TranslatedId:", currentId)
        tNames.append(variable.name)
        tIds.append(currentId)
    
    #Translating Actions
    for action in testCase.actions:
        if action.action == "click":
            currentAction ="click()"
        elif action.action == "sendKeys":
            currentAction = "replaceText(\""+ action.actionValue +"\"), closeSoftKeyboard()"
        tActionNames.append(action.name)
        tActionActions.append(currentAction)
    
    #Translating Assertions
    for assertion in testCase.assertions:
        if assertion.assertionAction == "getText":
            currentAssertion = "withText(\"" + assertion.assertionValue + "\")"
        if assertion.assertionType == "assertEquals":
            currentAssertionFull = "matches("+ currentAssertion + ")"
        tAssertionNames.append(assertion.name)
        tAssertionActions.append(currentAssertionFull)
    
    #Creating Translated Test Case
    for i in range(len(tNames)):
        #print("Translated Variable Name:", tNames[i])
        #print("Translated Variable Id:", tIds[i])
        tVariable = TranslatedVariables(tNames[i], tIds[i])
        translatedTestCase.tVariables.append(tVariable)
    for i in range(len(tActionNames)):
        #print("Translated Action Name:", tActionNames[i])
        #print("Translated Action Action:", tActionActions[i])
        tAction = TranslatedActions(tActionNames[i], tActionActions[i])
        translatedTestCase.tActions.append(tAction)
    for i in range(len(tAssertionNames)):
        #print("Translated Assertion Name:", tAssertionNames[i])
        #print("Translated Assertion Action:", tAssertionActions[i])
        tAssertion = TranslatedAssertions(tAssertionNames[i], tAssertionActions[i])
        translatedTestCase.tAssertions.append(tAssertion)

''' Object Print Debugging Statements
for item in translatedTestCaseObjects:
    print("Translated Test Case Name:", item.name)
    print("Translated Test Case Structure:", item.structure)
    for variable in item.tVariables:
        print("Translated Test Case Variable Name:", variable.name)
        print("Translated Test Case Variable Id:", variable.vId)
    for actions in item.tActions:
        print("Translated Test Case Action Name:", actions.name)
        print("Translated Test Case Action Action:", actions.action)
    for assertions in item.tAssertions:
        print("Translated Test Case Assertion Name:", assertions.name)
        print("Translated Test Case Assertion Action:", assertions.assertion)
    print("\n")
'''    
#-----------------------------

espressoCode = ekencoder(translatedTestCaseObjects) #eke = espresso kotlin encoder

outputFile = "testingMaterial/espressoTests/v2Translations/translatedCodeAttempt4.kt" #CHANGE THE OUTPUT FILE HERE
with open(outputFile, 'w+') as file:
    file.writelines(espressoCode)
        
        


