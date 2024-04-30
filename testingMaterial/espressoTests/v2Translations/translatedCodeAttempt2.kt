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
    fun SingleButton(){
       valbutton = onView(findElement(Locator.ID, "buttonID"))
       valmsg = onView(findElement(Locator.ID, "msgID"))
       button.perform(click())
       msg.check(matches(withText("Button has been pressed 1 time")))
       button.perform(click())
       msg.check(matches(withText("Button has been pressed 2 times")))
       button.perform(click())
       msg.check(matches(withText("Button has been pressed 3 times")))

    }
}