package com.example.dissertationdummyapp


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
    var mActivityScenarioRule = ActivityScenarioRule(LoginActivity::class.java)

    //Login Tests
    @Test
    fun loginSuccess() {
        val username = onView(withId(R.id.usernameTextField))
        username.perform(replaceText("testuser"), closeSoftKeyboard())

        val password = onView(withId(R.id.passwordTextField))
        password.perform(replaceText("testpass"), closeSoftKeyboard())

        val submit = onView(withId(R.id.submitButton))
        submit.perform(click())

        val successMessage = onView(withId(R.id.successMsg))
        successMessage.check(matches(withText("Welcome testuser!")))
    }

    @Test
    fun loginFail() {
        val username = onView(withId(R.id.usernameTextField))
        username.perform(replaceText("testuser"), closeSoftKeyboard())

        val submit = onView(withId(R.id.submitButton))
        submit.perform(click())

        val errorMessage = onView(withId(R.id.errorTextView))
        errorMessage.check(matches(withText("Please enter valid username and password")))
    }

    //Sign Up Tests
    @Test
    fun signUpPageSuccess() {
        val signupbtn = onView(withId(R.id.signupbutton))
        signupbtn.perform(click())

        val email = onView(withId(R.id.emailTextField))
        email.perform(replaceText("test@email.com"))

        val username = onView(withId(R.id.usernameTextField))
        username.perform(replaceText("testuser"))

        val password = onView(withId(R.id.passwordTextField))
        password.perform(replaceText("testpass"))

        val confirmPassword = onView(withId(R.id.confirmpTextField))
        confirmPassword.perform(replaceText("testpass"))

        val submit = onView(withId(R.id.submitButton))
        submit.perform(click())

        val successMessage = onView(withId(R.id.successMsg))
        successMessage.check(matches(withText("Welcome testuser!")))
    }

    @Test
    fun signUpPageIncompleteFields(){
        val signupbtn = onView(withId(R.id.signupbutton))
        signupbtn.perform(click())

        val email = onView(withId(R.id.emailTextField))
        email.perform(replaceText("test@email.com"))

        val username = onView(withId(R.id.usernameTextField))
        username.perform(replaceText("testuser"))

        val password = onView(withId(R.id.passwordTextField))
        password.perform(replaceText("testpass"))

        val submit = onView(withId(R.id.submitButton))
        submit.perform(click())

        val errorMessage = onView(withId(R.id.errorTextView))
        errorMessage.check(matches(withText("Please complete all fields")))

    }

    @Test
    fun signUpEmailFailure(){
        val signupbtn = onView(withId(R.id.signupbutton))
        signupbtn.perform(click())

        val email = onView(withId(R.id.emailTextField))
        email.perform(replaceText("test@emailcom"))

        val username = onView(withId(R.id.usernameTextField))
        username.perform(replaceText("testuser"))

        val password = onView(withId(R.id.passwordTextField))
        password.perform(replaceText("testpass"))

        val confirmPassword = onView(withId(R.id.confirmpTextField))
        confirmPassword.perform(replaceText("testpass"))

        val submit = onView(withId(R.id.submitButton))
        submit.perform(click())

        val errorMessage = onView(withId(R.id.errorTextView))
        errorMessage.check(matches(withText("Please enter a valid email address")))
    }

    @Test
    fun signUpPasswordFailure() {
        val signupbtn = onView(withId(R.id.signupbutton))
        signupbtn.perform(click())

        val email = onView(withId(R.id.emailTextField))
        email.perform(replaceText("test@email.com"))

        val username = onView(withId(R.id.usernameTextField))
        username.perform(replaceText("testuser"))

        val password = onView(withId(R.id.passwordTextField))
        password.perform(replaceText("testpass"))

        val confirmPassword = onView(withId(R.id.confirmpTextField))
        confirmPassword.perform(replaceText("testpass1"))

        val submit = onView(withId(R.id.submitButton))
        submit.perform(click())

        val errorMessage = onView(withId(R.id.errorTextView))
        errorMessage.check(matches(withText("Passwords do not match")))
    }

    @Test
    fun signUpEmailAndPasswordFailure(){
        val signupbtn = onView(withId(R.id.signupbutton))
        signupbtn.perform(click())

        val email = onView(withId(R.id.emailTextField))
        email.perform(replaceText("testemailcom"))

        val username = onView(withId(R.id.usernameTextField))
        username.perform(replaceText("testuser"))

        val password = onView(withId(R.id.passwordTextField))
        password.perform(replaceText("testpass"))

        val confirmPassword = onView(withId(R.id.confirmpTextField))
        confirmPassword.perform(replaceText("testpass1"))

        val submit = onView(withId(R.id.submitButton))
        submit.perform(click())

        val errorMessage = onView(withId(R.id.errorTextView))
        errorMessage.check(matches(withText("Please check email and password fields")))
    }

    @Test
    fun successPageLogout(){
        val username = onView(withId(R.id.usernameTextField))
        username.perform(replaceText("testuser"), closeSoftKeyboard())

        val password = onView(withId(R.id.passwordTextField))
        password.perform(replaceText("testpass"), closeSoftKeyboard())

        val submit = onView(withId(R.id.submitButton))
        submit.perform(click())

        val successMessage = onView(withId(R.id.successMsg))
        successMessage.check(matches(withText("Welcome testuser!")))

        val logout = onView(withId(R.id.submitButton))
        logout.perform(click())
    }
}

