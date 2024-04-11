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
        val username = onView(withId(R.id.usernameTextField))
        username.perform(replaceText("dimbo"), closeSoftKeyboard())
        val password = onView(withId(R.id.passwordTextField))
        password.perform(replaceText("dimbo"), closeSoftKeyboard())
        val submit = onView(withId(R.id.submitButton))
        submit.perform(click())
        val successMsg = onView(withId(R.id.successMsg))
        successMsg.check(matches(withText("welcome dimbo!")))
    } 


    @Test
    fun LoginFailure(){
        val submit = onView(withId(R.id.submitButton))
        submit.perform(click())
        val successMsg = onView(withId(R.id.successMsg))
        successMsg.check(matches(withText("welcome dimbo!")))
    } 


    @Test
    fun SignUpPageSucess(){
        val el1 = onView(withId(R.id.signupbutton))
        el1.perform(click())
        val el2 = onView(withId(R.id.emailTextField))
        el2.perform(replaceText("dimbo@dimbo.com"), closeSoftKeyboard())
        val el3 = onView(withId(R.id.usernameTextField))
        el3.perform(replaceText("dimbo"), closeSoftKeyboard())
        val el4 = onView(withId(R.id.passwordTextField))
        el4.perform(replaceText("dimbopass"), closeSoftKeyboard())
        val el5 = onView(withId(R.id.confirmpTextField))
        el5.perform(replaceText("dimbopass"), closeSoftKeyboard())
        val el6 = onView(withId(R.id.submitButton))
        el6.perform(click())
        val el7 = onView(withId(R.id.successMsg))
        el7.check(matches(withText("welcome dimbo!")))
    } 
}