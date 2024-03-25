import javalang
import javalang.tokenizer
from TestCase import TestCase

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
    testCases = []
    for i in range(len(testTokens)):
        if testTokens[i].value == "public" and testTokens[i+1].value == "void":
            test_case = TestCase()
            test_case.name = testTokens[i+2].value
            testCases.append(test_case)
    return testCases

def getVariableNames(testTokens):
    variables = []
    keywords = ["int", "String", "float", "double", "boolean", "char", "WebElement", "val"]
    for i in range(len(testTokens)):
        if testTokens[i].value in keywords and testTokens[i+1].value == "=":
            variables.append(testTokens[i+2].value)
    return variables


# Example usage
file_name = "appiumTests/AppiumTrialLevel3.java"
alltokens = tokenize_java_file(file_name)
testTokens = extract_test_cases(alltokens)
testCases = getTestCaseNames(testTokens)
variables = getVariableNames(testTokens)

for test_case in testCases:
    print("Test Name:", test_case.name)
    print("Variables:", test_case.variables)
    print("Assertions:", test_case.assertions)
    print("Actions:", test_case.actions)
    print("\n")

print("Variables:", variables)