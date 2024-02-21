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
    fun LoginPageError(){
        val submit = onView(withId(R.id.AppiumBy.id("com.example.dissertationdummyapp:id/submitButton")))
        submitclick()


    @Test
    fun SignUpPageSuccess(){
        val email = onView(withId(R.id.AppiumBy.xpath("//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.EditText[1]")))
        emailsendKeys("email@email.com")
        val username = onView(withId(R.id.AppiumBy.xpath("//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.EditText[2]")))
        usernamesendKeys("username")
        val password = onView(withId(R.id.AppiumBy.xpath("//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.EditText[3]")))
        passwordsendKeys("password")
        val cpassword = onView(withId(R.id.AppiumBy.xpath("//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.EditText[4]")))
        cpasswordsendKeys("password")
        val signUpButton = onView(withId(R.id.AppiumBy.xpath("//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]")))
        signUpButtonclick()
        val successMessage = onView(withId(R.id.AppiumBy.xpath("//android.widget.TextView[@text=\"Welcome test\"]")))
        successMessageXXX
