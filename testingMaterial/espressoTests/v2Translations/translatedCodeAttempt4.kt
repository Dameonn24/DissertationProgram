import androidx.test.espresso.Espresso.onView
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
        var mActivityScenarioRule = ActivityScenarioRule(MainActivity::class.java) 

    @Test
    fun LoginSuccess(){
       val username = onView(findElement(Locator.ID, "usernameTextField"))
       username.perform(replaceText("dimbousername"), closeSoftKeyboard())
       username.perform(click())
       username.check(matches(withText("dimbousername")))
       val password = onView(findElement(Locator.ID, "passwordTextField"))
       password.perform(replaceText("dimbopassword"), closeSoftKeyboard())
       val submit = onView(findElement(Locator.ID, "submitButton"))
       submit.perform(click())
       password.perform(replaceText("dimbopasswordpt2"), closeSoftKeyboard())
       val successMsg = onView(findElement(Locator.ID, "successMsgID"))
       successMsg.check(matches(withText("welcome dimbo!")))
    }

    @Test
    fun LoginFailure(){
       val submit = onView(findElement(Locator.ID, "submitButton"))
       submit.perform(click())
       val successMsg = onView(findElement(Locator.ID, "successMsgID"))
       successMsg.check(matches(withText("Please fill all the fields")))
    }

    @Test
    fun SignUpPageSucess(){
       val el1 = onView(findElement(Locator.ID, "signupbutton"))
       el1.perform(click())
       val el2 = onView(findElement(Locator.ID, "emailTextField"))
       el2.perform(replaceText("dimbo@dimbo.com"), closeSoftKeyboard())
       val el3 = onView(findElement(Locator.ID, "usernameTextField"))
       el3.perform(replaceText("dimbousername"), closeSoftKeyboard())
       val el4 = onView(findElement(Locator.ID, "passwordTextField"))
       el4.perform(replaceText("dimbopass"), closeSoftKeyboard())
       val el5 = onView(findElement(Locator.ID, "confirmpTextField"))
       el5.perform(replaceText("dimbocpass"), closeSoftKeyboard())
       val el6 = onView(findElement(Locator.ID, "submitButton"))
       el6.perform(click())
       val el7 = onView(findElement(Locator.ID, "successMsgID"))
       el7.check(matches(withText("Welcome dimbo!")))
       el3.check(matches(withText("dimboagain")))
    }
}