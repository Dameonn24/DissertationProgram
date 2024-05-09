//Test File created using Appium-Espresso Translator. © Dimasha Fernando 2024
package com.example.dissertationdummyapp

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
class TranslatedAppiumTrialLevel2 {

    @Rule
    @JvmField
    var mActivityScenarioRule = ActivityScenarioRule(LoginActivity::class.java)

    @Test
    fun loginPageSuccess(){
        val username = onView(withId(R.id.usernameTextField))
        username.perform(replaceText("dimbo"), closeSoftKeyboard())
        val password = onView(withId(R.id.passwordTextField))
        password.perform(replaceText("dimbo"), closeSoftKeyboard())
        val submit = onView(withId(R.id.submitButton))
        submit.perform(click())
        val successMsg = onView(withId(R.id.successMsgID))
        val successAssertMsg = onView(withText("welcome dimbo!"))
        successMsg.check(matches(withText("welcome dimbo!")))
        successAssertMsg.check(matches(withText("under the sea")))
    }
}