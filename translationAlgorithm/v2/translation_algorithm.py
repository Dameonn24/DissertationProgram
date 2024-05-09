import javalang
import javalang.tokenizer
from TestObjects import *
from AJDecoder import *
from EKEncoder import *
import re

#file_name = "/Users/dimashafernando/AndroidStudioProjects/DissertationDummyApp2/app/src/androidTest/java/com/example/dissertationdummyapp/InitialTest.java" #CHANGE THE INPUT FILE HERE
file_name = "testingMaterial/appiumTests/AppiumTrialLevel2.java" #For testing purposes
alltokens = tokenize_java_file(file_name)
testTokens, testClassName, package = extract_test_cases(alltokens)
testCaseObjects = getTestCaseNames(testTokens)
decodedTestFile = ajdecoder(testTokens, testCaseObjects, testClassName, package) #ajd = appium java decoder

#-----------------------------
#TRANSLATION ALGORITHM
#Phrase Dictionary
def getTranslations(translatee):
    translations={
        #Variable Types
        "id":"withId(R.id.",
        "xpath":"withText(\"",
        #Actions
        "sendKeys" : "replaceText(\"{}\"), closeSoftKeyboard()",
        "click" : "click()",
        #Assertions
        "getText" : "withText(\"",
        "assertEquals" : "matches("
    }
    return translations.get(translatee, None)

#Actual Translation Algorithm
translatedTestCaseObjects = []
ajdTestCases = decodedTestFile.testCases
for testCase in ajdTestCases:
    translatedTestCaseName = testCase.name[0].lower()+testCase.name[1:] #Converting the first letter of the test case name to lowercase
    translatedTestCase = TranslatedTestCase(translatedTestCaseName, testCase.structure, [], [], [])
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
        tVariableId = ""
        #print("Variable Name:", variable.name)
        #print("Variable Type:", variable.vIdType)
        #print("Variable IdType:", variable.vIdType)
        currentId  = getTranslations(variable.vIdType)
        if variable.vIdType == "xpath":
            #print("Variable Id:", variable.vId)
            for i in range(len(variable.vId)):
                if variable.vId[i] == "\"":
                    while variable.vId[i+1] != "]":
                        tVariableId = tVariableId + variable.vId[i+1]
                        i+=1
            tVariableId = tVariableId[:-2]+"\""
        else:
            tVariableId = variable.vId
        currentId = currentId + tVariableId+ ")"
        tNames.append(variable.name)
        tIds.append(currentId)
    
    #Translating Actions
    for action in testCase.actions:
        currentAction = getTranslations(action.action).format(action.actionValue)
        tActionNames.append(action.name)
        tActionActions.append(currentAction)
    
    #Translating Assertions
    for assertion in testCase.assertions:
        currentAssertion = getTranslations(assertion.assertionType) + getTranslations(assertion.assertionAction) + assertion.assertionValue + "\"))"
        tAssertionNames.append(assertion.name)
        tAssertionActions.append(currentAssertion)
    
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
translatedTestCaseFile = TestFile(decodedTestFile.name, decodedTestFile.package, translatedTestCaseObjects) #Creating the new testcase file 

'''
#Object Print Debugging Statements
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

espressoCode = ekencoder(translatedTestCaseFile) #eke = espresso kotlin encoder

#outputFile = "/Users/dimashafernando/AndroidStudioProjects/DissertationDummyApp2/app/src/androidTest/java/com/example/dissertationdummyapp/Translated"+decodedTestFile.name+"EspressoTest.kt" #CHANGE THE OUTPUT FILE HERE
outputFile = "testingMaterial/espressoTests/Translated"+decodedTestFile.name+"KotlinTest.kt" #For testing purposes
with open(outputFile, 'w+') as file:
    file.writelines(espressoCode)

print("Translation Completed!")



