package com.example.dissertationdummyapp;

import io.appium.java_client.AppiumBy;
import io.appium.java_client.remote.options.BaseOptions;
import io.appium.java_client.android.AndroidDriver;

import java.net.MalformedURLException;
import java.net.URL;
import java.util.Objects;

import org.junit.Assert;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.openqa.selenium.WebElement;

public class TestAppium {

    private AndroidDriver driver;

    @BeforeEach
    public void setUp() {
        BaseOptions options = new BaseOptions()
                .amend("platformName", "Android")
                .amend("appium:automationName", "UiAutomator2")
                .amend("appium:platformVersion", "14.0")
                .amend("appium:deviceName", "Pixel 7 API 34")
                .amend("appium:udid", "emulator-5554")
                .amend("appium:appPackage", "com.example.dissertationdummyapp")
                .amend("appium:appActivity", ".LoginActivity")
                .amend("appium:noReset", "true")
                .amend("appium:ensureWebviewsHavePages", true)
                .amend("appium:nativeWebScreenshot", true)
                .amend("appium:newCommandTimeout", 3600)
                .amend("appium:connectHardwareKeyboard", true);

        /*
         * driver = new AndroidDriver((this.getUrl()), options);
         * }
         * 
         * private URL getUrl() {
         * try {
         * return new URL("http://143.167.122.152:4723/");
         * } catch (MalformedURLException e) {
         * e.printStackTrace();
         * }
         * return null;
         * }
         */
        driver = new AndroidDriver(this.getUrl(), options);
    }

    private URL getUrl() {
        try {
            return new URL("http://127.0.0.1:4723");
        } catch (MalformedURLException e) {
            e.printStackTrace();
        }
        return null;
    }

    @Test
    public void LoginSuccess() {
        WebElement username = driver.findElement(AppiumBy.id("com.example.dissertationdummyapp:id/usernameTextField"));
        username.sendKeys("dimbo");
        username.click();
        WebElement password = driver.findElement(AppiumBy.id("com.example.dissertationdummyapp:id/passwordTextField"));
        password.sendKeys("dimbo");
        WebElement submit = driver.findElement(AppiumBy.id("com.example.dissertationdummyapp:id/submitButton"));
        submit.click();
        password.sendKeys("dimbo");
        WebElement successMsg = driver.findElement(AppiumBy.id("com.example.dissertationdummyapp:id/successMsgID"));
        Assert.assertEquals(successMsg.getText(), "welcome dimbo!");
    }

    @Test
    public void LoginFailure() {
        WebElement submit = driver.findElement(AppiumBy.id("com.example.dissertationdummyapp:id/submitButton"));
        submit.click();
        WebElement successMsg = driver.findElement(AppiumBy.id("com.example.dissertationdummyapp:id/successMsg"));
        Assert.assertEquals(successMsg.getText(), "Please fill all the fields");
    }

    @Test
    public void SignUpPageSucess() {
        WebElement el1 = driver.findElement(AppiumBy.id("com.example.dissertationdummyapp:id/signupbutton"));
        el1.click();
        WebElement el2 = driver.findElement(AppiumBy.id("com.example.dissertationdummyapp:id/emailTextField"));
        el2.sendKeys("dimbo@dimbo.com");
        WebElement el3 = driver.findElement(AppiumBy.id("com.example.dissertationdummyapp:id/usernameTextField"));
        el3.sendKeys("dimbo");
        WebElement el4 = driver.findElement(AppiumBy.id("com.example.dissertationdummyapp:id/passwordTextField"));
        el4.sendKeys("dimbopass");
        WebElement el5 = driver.findElement(AppiumBy.id("com.example.dissertationdummyapp:id/confirmpTextField"));
        el5.sendKeys("dimbopass");
        WebElement el6 = driver.findElement(AppiumBy.id("com.example.dissertationdummyapp:id/submitButton"));
        el6.click();
        WebElement el7 = driver.findElement(AppiumBy.id("com.example.dissertationdummyapp:id/successMsg"));
        Assert.assertEquals(el7.getText(), "Welcome dimbo!");

    }

    @AfterEach
    public void tearDown() {
        driver.quit();
    }
}
