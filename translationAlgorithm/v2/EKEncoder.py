import re
    
def ekencoder (translatedTestCaseFile):
    espressoCode = """//Test File created using Appium-Espresso Translator. © Dimasha Fernando 2024
package """+translatedTestCaseFile.package+"""

import androidx.test.espresso.Espresso.onView
import androidx.test.espresso.action.ViewActions.click
import androidx.test.espresso.action.ViewActions.closeSoftKeyboard
import androidx.test.espresso.action.ViewActions.replaceText
import androidx.test.espresso.assertion.ViewAssertions.matches
import androidx.test.espresso.matcher.ViewMatchers.withId
import androidx.test.espresso.matcher.ViewMatchers.withText
import androidx.test.ext.junit.rules.ActivityScenarioRule
import androidx.test.ext.junit.runners.AndroidJUnit4
import androidx.test.filters.LargeTest
import org.junit.Rule
import org.junit.Test
import org.junit.runner.RunWith

@LargeTest
@RunWith(AndroidJUnit4::class)
class Translated"""+translatedTestCaseFile.name+""" {

    @Rule
    @JvmField
    var mActivityScenarioRule = ActivityScenarioRule(LoginActivity::class.java)"""
    translatedTestCaseObjects = translatedTestCaseFile.testCases
    for testCase in translatedTestCaseObjects:
        espressoCode += "\n\n    @Test\n    fun " + testCase.name + "(){\n"
        for i, item in enumerate(testCase.structure):
            match = re.match(r'([A-Za-z]+)([0-9]+)', item)
            lineType = match.group(1)
            index = int(match.group(2))
            if lineType == "V":
                currentLine = "        val "+ testCase.tVariables[index].name + " = onView(" + testCase.tVariables[index].vId + ")\n"
                espressoCode += currentLine
            elif lineType == "AV":
                currentLine = "        " + testCase.tActions[index].name + ".perform(" + testCase.tActions[index].action + ")\n"
                espressoCode += currentLine
            elif lineType == "A":
                currentLine = "        " + testCase.tAssertions[index].name + ".check(" + testCase.tAssertions[index].assertion + ")\n"
                espressoCode += currentLine
        espressoCode += "    }"
    espressoCode += "\n}"
    return espressoCode