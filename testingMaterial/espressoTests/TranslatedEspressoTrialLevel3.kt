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
    fun LoginPageSuccess(){
       val username = onView(withId(R.ID. "usernameTextField"))
       username.perform(replaceText("dimbo"), closeSoftKeyboard())
       val password = onView(withId(R.ID. "passwordTextField"))
       password.perform(replaceText("dimbo"), closeSoftKeyboard())
       val submit = onView(withId(R.ID. "submitButton"))
       submit.perform(click())
       val successMsg = onView(withId(R.ID. "successMsgID"))
       val successAssertMsg = onView(withText("welcome dimbo!"))
       successMsg.check(matches(withText("welcome dimbo!")))
       successAssertMsg.check(matches(withText("under the sea")))
    }
}