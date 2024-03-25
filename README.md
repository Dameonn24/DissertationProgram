
# Automatic Translation of Appium Test Cases to Espresso Test Cases for an Android Mobile Application

This is my Dissertation Project. It works by taking the Appium test file that needs to be translated (Source file) and then dissecting it into its key test information using the Appium - Java Decoder (AJD). 

The AJD then passes the information to the translation algorithm (TA) in which all Java - specific code is converted into Kotlin - specific code. 

This translated code and information is then sent to the Espresso - Kotlin Encoder (EKE). The EKE then wraps the test information with the Kotlin - specific code and then additional code around it to create a final Espresso test file written in Kotlin, ready for use. 



## Project Structure

The repository has three "areas" of concern:   
    1. The translation algorithm (stored in "translationAlgorithm".)  
    2. The appium files to be translated (stored in "appiumTests".)   
    3. the translated espresso files (stored in "espressoTests".)  

The translation algorithm has two versions:  
- version 1 (translation_algorithm.py)  
- version 2 (stored in folder "v2")  

Version 1 runs the AJD, TA and EKE all in one script.

In version 2, I am trying to create a class called "TestCase" that creates an test case object for each test case in the source file.

Version 2 contains two files:  
    1. TestCase.py - this holds the class TestCase.  
    2. translation_algoV2.py - this holds a newer version of the TA code trying to incorporate the class TestCase. 

## Deployment

To deploy this project

Open it in your IDE (e.g. Visual Studio Code) and run the script as a normal python file. 

To check that translation_algorithm.py (Verion 1) is properly working, go to line 259 and change the file name (in this case "translatedCodev5.kt") to whatever you want. 

```
outputFile = "espressoTests/translatedCodev5.kt"

```

If you run the script with a new file name, it should appear in your espressoTests folder. 

Version 2 is currently in developement, so it will give you an error. 

To run Version 2, go to translation_algoV2.py and run it like a normal python script.
