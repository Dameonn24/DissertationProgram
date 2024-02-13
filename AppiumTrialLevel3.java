package com.example.dissertationdummyapp;

// This sample code supports Appium Java client >=9
// https://github.com/appium/java-client

import io.appium.java_client.AppiumBy;
import io.appium.java_client.android.AndroidDriver;

import java.net.MalformedURLException;
import java.net.URL;

import org.junit.After;
import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;
import org.openqa.selenium.*;
import org.openqa.selenium.remote.DesiredCapabilities;

public class AppiumTrialLevel3 {
        private AndroidDriver driver;

        @Before
        public void setup() throws MalformedURLException {
                DesiredCapabilities caps = new DesiredCapabilities();
                caps.setCapability("platformName", "Android");
                caps.setCapability("automationName", "UiAutomator2");
                caps.setCapability("platformVersion", "14.0");
                caps.setCapability("deviceName", "Pixel 7 API 34");
                caps.setCapability("udid", "emulator-5554");
                caps.setCapability("appPackage", "com.example.dissertationdummyapp");
                caps.setCapability("appActivity", ".MainActivity");
                caps.setCapability("noReset", "true");
                caps.setCapability("ensureWebviewsHavePages", true);
                caps.setCapability("nativeWebScreenshot", true);
                caps.setCapability("newCommandTimeout", 3600);
                caps.setCapability("connectHardwareKeyboard", true);

                AndroidDriver driver = new AndroidDriver(new URL("http://127.0.0.1:4723/wd/hub"), caps);
                /*
                 * try {
                 * driver = new AndroidDriver(new URL("http://127.0.0.1:4723/wd/hub"), caps);
                 * } catch (MalformedURLException e) {
                 * e.printStackTrace();
                 * }
                 */
        }

        // START OF TESTS

        // Login Page Tests
        @Test
        public void LoginPageError() {
                WebElement submit = driver.findElement(AppiumBy.id("com.example.dissertationdummyapp:id/submitButton"));
                submit.click();
                Assert.assertEquals(submit.getText(), "Please fill in all the fields");
                assert submit.getText().equals("Please fill in all the fields");
        }

        // SignUp Page Tests
        @Test
        public void SignUpPageSuccess() {
                WebElement email = driver.findElement(AppiumBy.xpath(
                                "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.EditText[1]"));
                email.sendKeys("email@email.com");
                WebElement username = driver.findElement(AppiumBy.xpath(
                                "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.EditText[2]"));
                username.sendKeys("username");
                WebElement password = driver.findElement(AppiumBy.xpath(
                                "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.EditText[3]"));
                password.sendKeys("password");
                WebElement cpassword = driver.findElement(AppiumBy.xpath(
                                "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.EditText[4]"));
                cpassword.sendKeys("password");
                WebElement signUpButton = driver.findElement(AppiumBy.xpath(
                                "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]"));
                signUpButton.click();
                WebElement successMessage = driver
                                .findElement(AppiumBy.xpath("//android.widget.TextView[@text=\"Welcome test\"]"));
                Assert.assertEquals(successMessage.getText(), "Welcome username");
        }

        // END OF TESTS

        @After
        public void tearDown() {
                driver.quit();
        }
}
