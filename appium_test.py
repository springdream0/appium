from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['automationName'] = 'uiautomator2'
desired_caps['appium:platformVersion'] = '12'
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = 'com.android.settings.Settings'
desired_caps['appium:deviceName'] = "4723"
desired_caps['systemPort'] = "8202"

desired_caps['appium:udid'] = "모바일단말기"


    
    
desired_caps = UiAutomator2Options().load_capabilities(desired_caps) 


line_value = 'http://localhost:4723/wd/hub'
line_value = 'http://localhost:4723'
driverTemp = webdriver.Remote(line_value, options=desired_caps)

sleep(5)