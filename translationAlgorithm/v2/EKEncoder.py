import re
    
def ekencoder (translatedTestCaseObjects):
    espressoCode = """import androidx.test.espresso.Espresso.onView
    import androidx.test.espresso.action.ViewActions.*
    import androidx.test.espresso.assertion.ViewAssertions.*
    import androidx.test.espresso.matcher.ViewMatchers.*
    import androidx.test.ext.junit.rules.ActivityScenarioRule
    import androidx.test.ext.junit.runners.AndroidJUnit4
    import androidx.test.filters.LargeTest
    import org.junit.Rule
    import org.junit.Test
    import org.junit.runner.RunWith

    @LargeTest
    @RunWith(AndroidJUnit4::class)
    class EspressoTests {

        @Rule
        @JvmField
        var mActivityScenarioRule = ActivityScenarioRule(MainActivity::class.java) """
    for testCase in translatedTestCaseObjects:
        espressoCode += "\n\n    @Test\n    fun " + testCase.name + "(){\n"
        for i, item in enumerate(testCase.structure):
            match = re.match(r'([A-Za-z]+)([0-9]+)', item)
            lineType = match.group(1)
            index = int(match.group(2))
            #print(item, lineType, index)
            if lineType == "V":
                currentLine = "       val "+ testCase.tVariables[index].name + " = onView(" + testCase.tVariables[index].vId + ")\n"
                espressoCode += currentLine
            elif lineType == "AV":
                currentLine = "       " + testCase.tActions[index].name + ".perform(" + testCase.tActions[index].action + ")\n"
                espressoCode += currentLine
            elif lineType == "A":
                currentLine = "       " + testCase.tAssertions[index].name + ".check(" + testCase.tAssertions[index].assertion + ")\n"
                espressoCode += currentLine
        espressoCode += "    }"
    espressoCode += "\n}"
    return espressoCode