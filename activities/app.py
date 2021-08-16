from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException
from loguru import logger

from conf.conf import TIMEOUT_FIND_LOCATOR


class App:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, timeout=TIMEOUT_FIND_LOCATOR):
        ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)
        wait = WebDriverWait(driver=self.driver, timeout=int(timeout), ignored_exceptions=ignored_exceptions)

        try:
            return wait.until(EC.visibility_of_element_located(locator))

        except Exception as e:
            logger.critical("Could not locate element with value: %s" % str(locator))
            raise NoSuchElementException("Could not locate element with value: %s" % str(locator))

    def find_elements(self, locator, timeout=TIMEOUT_FIND_LOCATOR):
        ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)
        wait = WebDriverWait(driver=self.driver, timeout=int(timeout), ignored_exceptions=ignored_exceptions)
        try:
            return wait.until(EC.visibility_of_all_elements_located(locator))
        except TimeoutException as e:
            logger.critical("Could not locate element with value: %s" % str(locator))
            raise NoSuchElementException("Could not locate element with value: %s" % str(locator))

    def tap(self, locator):
        element = self.find_element(locator)
        actions = TouchAction(self.driver)
        actions.tap(element)
        actions.perform()

    def enter_text(self, locator, text):
        self.find_element(locator).clear().send_keys(text)

    def click(self, locator):
        self.find_element(locator).click()

    def get_current_activity(self):
        return self.driver.current_activity

    def send_keys_to_multiple_inputs(self, locator, text):
        edit_texts = self.find_elements(locator)
        limit = len(edit_texts)

        for index in range(limit):
            edit_texts[index].clear().send_keys(text[index])

    def get_text(self, locator):
        el = self.find_element(locator)
        return el.text

    def is_element_displayed(self, locator):
        return self.find_element(locator).is_displayed()

    def is_element_enabled(self, locator):
        return self.find_element(locator).is_enabled()

