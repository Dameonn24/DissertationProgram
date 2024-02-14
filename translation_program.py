# THIS FILE IS NO LONGER IN USE




#APPIUM - JAVA DECODER
#Task - Breakdown the Appium file into all its test cases and then file the variables, actions and assertions made in each test case

#Read the file
#appiumFile = "/Users/dimashafernando/DissertationDummyApp/app/src/test/java/com/example/dissertationdummyapp/AppiumTest.java"
appiumFile = "AppiumTrialLevel1.java" #Training files
with open(appiumFile, 'r') as file:
    content = file.readlines()
 
#Initialise arrays
testCases = []


testCaseIndex = []
index = 0
#find the index of the test cases
for line in content:
    if "@Test" in line:
        testCaseIndex.append(index)
    else:
        index = index + 1
print (testCaseIndex)

#store all the lines in the current test case

'''
for line in content:
    if "public void test" in line:
        currrentTest.append(line)
    elif "}" in line:
        currrentTest.append(line)
        testCases.append(currrentTest)

print ("Number of test cases: " + str(len(testCases)))
for test in testCases:
    print (test)
    print ("\n")
    
'''