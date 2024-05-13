import javalang
import javalang.tokenizer
from TestObjects import *
from AJDecoder import *
from translation_algorithm import *
from EKEncoder import *
import re

#file_name = "/Users/dimashafernando/AndroidStudioProjects/DissertationDummyApp2/app/src/androidTest/java/com/example/dissertationdummyapp/InitialTest.java" #CHANGE THE INPUT FILE HERE
file_name = "testingMaterial/appiumTests/AppiumTrialLevel2.java" #For testing purposes
alltokens = tokenize_java_file(file_name)
testTokens, testClassName, package = extract_test_cases(alltokens)
testCaseObjects = getTestCaseNames(testTokens)
decodedTestFile = ajdecoder(testTokens, testCaseObjects, testClassName, package) #ajd = appium java decoder
translatedTestCaseFile = translation(decodedTestFile) #Translation Algorithm
espressoCode = ekencoder(translatedTestCaseFile) #eke = espresso kotlin encoder
#outputFile = "/Users/dimashafernando/AndroidStudioProjects/DissertationDummyApp2/app/src/androidTest/java/com/example/dissertationdummyapp/Translated"+decodedTestFile.name+"EspressoTest.kt" #CHANGE THE OUTPUT FILE HERE
outputFileName = "Translated"+decodedTestFile.name+"KotlinTest.kt"
outputFile = "testingMaterial/espressoTests/"+outputFileName #For testing purposes
with open(outputFile, 'w+') as file:
    file.writelines(espressoCode)

print("Translation Completed!")