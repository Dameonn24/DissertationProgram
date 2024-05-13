import javalang
import javalang.tokenizer
from TestObjects import *


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
def translation(decodedTestFile):
    translatedTestCaseObjects = []
    ajdTestCases = decodedTestFile.testCases
    for testCase in ajdTestCases:
        translatedTestCaseName = testCase.name[0].lower()+testCase.name[1:] #Converting the first letter of the test case name to lowercase
        #testCase.name = testCase.name[0].lower()+testCase.name[1:] #Converting the first letter of the test case name to lowercase
        translatedTestCase = TranslatedTestCase(translatedTestCaseName, testCase.structure, [], [], [])
        translatedTestCaseObjects.append(translatedTestCase)
        
        tNames = []
        tVIdTypes=[]
        tIds = []
        tActionNames = []
        tActionActions = []
        tActionValues = []
        tAssertionNames = []
        tAssertionTypes = []
        tAssertionActions = []
        tAssertionValues = []
        #print("Test Case Name:", testCase.name)
        
        #Translating Variables
        for variable in testCase.variables:
            tVariableId = ""
            #print("Variable Name:", variable.name)
            #print("Variable Type:", variable.vIdType)
            #print("Variable IdType:", variable.vIdType)
            #currentId  = getTranslations(variable.vIdType)
            tVIdType = getTranslations(variable.vIdType)
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
            #currentId = currentId + tVariableId+ ")"
            tNames.append(variable.name)
            tVIdTypes.append(tVIdType)
            tIds.append(tVariableId)

            
        #Translating Actions
        for action in testCase.actions:
            tActionNames.append(action.name)
            tActionActions.append(getTranslations(action.action))
            tActionValues.append(action.actionValue)

            
        #Translating Assertions
        for assertion in testCase.assertions:
            tAssertionNames.append(assertion.name)
            tAssertionTypes.append(getTranslations(assertion.assertionType))
            tAssertionActions.append(getTranslations(assertion.assertionAction))
            tAssertionValues.append(assertion.assertionValue)
            
        #Creating Translated Test Case
        for i in range(len(tNames)):
            #print("Translated Variable Name:", tNames[i])
            #print("Translated Variable Id:", tIds[i])
            tVariable = Variable(tNames[i], tVIdTypes[i], tIds[i])
            translatedTestCase.tVariables.append(tVariable)
        for i in range(len(tActionNames)):
            #print("Translated Action Name:", tActionNames[i])
            #print("Translated Action Action:", tActionActions[i])
            tAction = Action(tActionNames[i], tActionActions[i], tActionValues[i])
            translatedTestCase.tActions.append(tAction)
        for i in range(len(tAssertionNames)):
            #print("Translated Assertion Name:", tAssertionNames[i])
            #print("Translated Assertion Action:", tAssertionActions[i])
            tAssertion = Assertion(tAssertionNames[i], tAssertionTypes[i], tAssertionActions[i], tAssertionValues[i])
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
    return translatedTestCaseFile




