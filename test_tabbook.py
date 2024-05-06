# This sample code uses the Appium python client v2
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
import pytest
import csv
# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

caps = {}
caps["platformName"] = "android"
caps["platformVersion"] = "13"
caps["appium:ensureWebviewsHavePages"] = True
caps["appium:nativeWebScreenshot"] = True
caps["appium:newCommandTimeout"] = 3600
caps["appium:connectHardwareKeyboard"] = True
number = ['zero', 'one', 'two', 'third', 'four', 'five', 'six', 'seven', 'eight', 'nine']


def get_csv():
    ans = []
    with open('data.csv') as file:
        csv_f = csv.reader(file)
        for line in csv_f:
            ans.append(line)
    return ans


@pytest.mark.parametrize('li', get_csv())
class TestAdd:

    def setup_method(self):
        print("NCAA")
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

    def teardown_method(self):
        print("NBA")
        self.driver.quit()

    def test_add(self, li):
        el1 = self.driver.find_element(by=AppiumBy.XPATH,
                                       value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ImageView")
        el1.click()
        el2 = self.driver.find_element(by=AppiumBy.XPATH,
                                       value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[16]/android.widget.FrameLayout/android.widget.ImageView")
        el2.click()
        for i in li[1]:
            el5 = self.driver.find_element(by=AppiumBy.ID, value="com.shark.jizhang:id/" + number[int(i)])
            el5.click()
        if li[2] == '+':
            el6 = self.driver.find_element(by=AppiumBy.ID, value="com.shark.jizhang:id/plus")
            el6.click()
        elif li[2] == '.':
            el6 = self.driver.find_element(by=AppiumBy.ID, value="com.shark.jizhang:id/point")
            el6.click()
        elif li[2] == '-':
            el6 = self.driver.find_element(by=AppiumBy.ID, value="com.shark.jizhang:id/minus")
            el6.click()
        elif li[2] == '=':
            el6 = self.driver.find_element(by=AppiumBy.ID, value="com.shark.jizhang:id/done")
            el6.click()
        for i in li[3]:
            el5 = self.driver.find_element(by=AppiumBy.ID, value="com.shark.jizhang:id/" + number[int(i)])
            el5.click()
        el6 = self.driver.find_element(by=AppiumBy.ID, value="com.shark.jizhang:id/done")
        el6.click()
        el6.click()
        assert 1


class TestRemove:
    def setup_method(self):
        print("NCAA")
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

    def teardown_method(self):
        print("NBA")
        self.driver.quit()

    def test_remove(self):
        el1 = self.driver.find_element(by=AppiumBy.XPATH,
                                       value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ImageView")
        el1.click()
        touch = TouchAction(self.driver)
        touch.long_press(x=86, y=690).perform()
        el = self.driver.find_element(by=AppiumBy.XPATH,
                                      value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView")
        el.click()
        assert 1


class TestCheck:
    def setup_method(self):
        print("NCAA")
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

    def teardown_method(self):
        print("NBA")
        self.driver.quit()

    def test_check_1(self):
        el1 = self.driver.find_element(by=AppiumBy.XPATH,
                                  value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ImageView")
        el1.click()
        el2 = self.driver.find_element(by=AppiumBy.ID, value="com.shark.jizhang:id/month")
        el2.click()
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(265, 347)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.pause(0.1)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        el3 = self.driver.find_element(by=AppiumBy.ID, value="com.shark.jizhang:id/leaderBoardTitle")
        el3.click()
        assert 1

    def test_check_2(self):
        el1 = self.driver.find_element(by=AppiumBy.XPATH,
                                       value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ImageView")
        el1.click()
        touch = TouchAction(self.driver)
        touch.long_press(x=86, y=690).perform()
        el2 = self.driver.find_element(by=AppiumBy.XPATH,
                                  value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[3]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView")
        el2.click()
        el3 = self.driver.find_element(by=AppiumBy.ID, value="com.shark.jizhang:id/shareBtn")
        el3.click()
        time.sleep(1)
        el4 = self.driver.find_element(by=AppiumBy.ID, value="com.shark.jizhang:id/RoundedImageView")
        el4.click()
        assert 1


if __name__ == '__main__':
    pytest.main(['-vs', 'test_tabbook.py'])
