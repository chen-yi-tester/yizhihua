from appium import webdriver
from page.main_page import MainPage


class App:
    driver: webdriver
    @classmethod
    def start(cls):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "sssss"
        caps["appPackage"] = "com.lxlg.spend.yw.user"
        caps["appActivity"] = "ui.main.MainActivity"
        caps["autoGrantPermissions"] = "true"
        caps["automationName"] = "UiAutomator2"
        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        cls.driver.implicitly_wait(5)
        return MainPage(cls.driver)