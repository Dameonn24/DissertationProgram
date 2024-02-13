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

public class AppiumTrialLevel1 {
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
    
    //START OF TESTS
    
    @Test
    public void LoginPageError() {
        WebElement el9 = driver.findElement(AppiumBy.xpath("//android.widget.TextView[@text=\"Please fill in all the fields\"]"));
        Assert.assertEquals(el9.getText(), "Please fill in all the fields");
    }

    //END OF TESTS

    @After
    public void tearDown() {
        driver.quit();
    }
}
