
# Appium to Espresso: Automatic Translation of UI Test Cases for an Android Mobile Application

This is my Dissertation Project. It works by taking the Appium test file that needs to be translated (Source file) and then dissecting it into its key test information using the Appium - Java Decoder (AJD). 

The AJD then passes the information to the translation algorithm (TA) in which all Java-specific code is converted into Kotlin-specific code. 

This translated code and information is then sent to the Espresso-Kotlin Encoder (EKE). The EKE then wraps the test information with the Kotlin-specific code and then additional code around it to create a final Espresso test file written in Kotlin, ready for use. 



## Project Structure

The repository has three "areas" of concern:   
    1. The translation algorithm (stored in "translationAlgorithm".)  
    2. The appium files to be translated (stored in "trainingMaterial/appiumTests".)   
    3. the translated espresso files (stored in "trainingMaterial/espressoTests".)  

The translation algorithm has two versions:  
- version 1 (stored in the folder "v1")  
- version 2 (stored in the folder "v2")  

Version 1 runs the AJD, TA and EKE all in one script.

In version 2, I am trying to create a class called "TestCase" that creates a test case object for each test case in the source file.

Version 2 contains the following files:  
    1. TestObject.py - this holds the classes for TestCase, Variable, InitialisedVariable and Assertions.  
    2. AJDecoder.py - this holds all the code for the Appium-Java Decoder. This portion of the code focuses on dissecting the Appium test cases into its core data to be passed into the translation algorithm.  
    3. translation_algorithm.py - this holds the java-to-kotlin translations.  
    4. EKEncoder.py - this holds all the code for the Espresso-Kotlin Encoder. This portion of the code focuses on wrapping the core data in Kotlin code according to the Espresso framework.   

## Deployment

### Version 2
To deploy this project
1. Open the project in your favourite IDE (e.g. Visual Studio Code)
2. Open the file A2E.py (found in ```DissertationProgram/translationAlgorithm/v2/A2E.py```)
3. Change the path to the input file of your choice (```Line 10 ```)
4. Change the path to the target location of your choice. Only change the destination path and not the file name (```Line 19```)
5. Run the script and enjoy!!

### Version 1
To deploy this project

Open it in your IDE (e.g. Visual Studio Code) and run the script as a normal Python file. 

To check that translation_algorithm.py (```translationAlgorithm/v1/translation_algorithm.py```) is properly working, go to line 259 and change the file name (in this case "translatedCodev5.kt") to whatever you want. 

```
outputFile = "espressoTests/translatedCodev5.kt"
```

If you run the script with a new file name, it should appear in your espressoTests folder. 
