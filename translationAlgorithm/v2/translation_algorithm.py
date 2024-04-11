import javalang
import javalang.tokenizer
from TestObjects import *
from AJDecoder import *
from EKEncoder import *

file_name = "testingMaterial/appiumTests/AppiumTrialLevel3.java"
alltokens = tokenize_java_file(file_name)
testTokens = extract_test_cases(alltokens)
testCaseObjects = getTestCaseNames(testTokens)
ajd = getVariablesAndAssertions(testTokens, testCaseObjects) #ajd = appium java decoder