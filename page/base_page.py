import random
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.remote.webdriver import WebDriver


class Basepage:
    __num1 = '181,1711'
    __num2 = '544,1720'
    __num3 = '889,1711'
    __num4 = '181,1870'
    __num5 = '536,1870'
    __num6 = '889,1870'

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_by_id(self, locat_id):
        return self.driver.find_element_by_id(locat_id)

    def get_toast(self):
        result = self.driver.find_element_by_xpath("//*[@class='android.widget.Toast']").text
        return result

    def get_x_locator(self, locator):
        loxy = tuple(eval(locator))
        return loxy[0]

    def get_y_locator(self, locator):
        loxy = tuple(eval(locator))
        return loxy[1]

    def touch_button(self, locator):
        sleep(1)
        TouchAction(self.driver).tap(x=self.get_x_locator(locator), y=self.get_y_locator(locator)).perform()

    def create_phone(self):
        second = [3, 4, 5, 7, 8][random.randint(0, 4)]
        third = {3: random.randint(0, 9),
                4: [5, 7, 9][random.randint(0, 2)],
                5: [i for i in range(10) if i != 4][random.randint(0, 8)],
                7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
                8: random.randint(0, 9),
                }[second]
        suffix = random.randint(9999999, 100000000)
        return "1{}{}{}".format(second, third, suffix)
    def pay_password(self):
        self.touch_button(self.__num1)
        sleep(1)
        self.touch_button(self.__num2)
        sleep(1)
        self.touch_button(self.__num3)
        sleep(1)
        self.touch_button(self.__num4)
        sleep(1)
        self.touch_button(self.__num5)
        sleep(1)
        self.touch_button(self.__num6)
    def get_text_by_id(self,id):
        sleep(3)
        text = self.driver.find_element_by_id(id).text
        return text