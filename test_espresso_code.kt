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
        
        val password = onView(withId(R.id.passwordTextField))
        
        val submit = onView(withId(R.id.submitButton))
        
        val successMsg = onView(withId(R.id.successMsg))
        


    @Test
    fun LoginFailure(){
        val submit = onView(withId(R.id.submitButton))
        
        val successMsg = onView(withId(R.id.successMsg))
        


    @Test
    fun SignUpPageSucess(){
        val el1 = onView(withId(R.id.signupbutton))
        
        val el2 = onView(withId(R.id.emailTextField))
        
        val el3 = onView(withId(R.id.usernameTextField))
        
        val el4 = onView(withId(R.id.passwordTextField))
        
        val el5 = onView(withId(R.id.confirmpTextField))
        
        val el6 = onView(withId(R.id.submitButton))
        
        val el7 = onView(withId(R.id.successMsg))
        
