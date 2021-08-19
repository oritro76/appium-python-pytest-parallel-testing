from datetime import datetime
import os
import base64
import io

from PIL import Image
from appium import webdriver
from loguru import logger
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, \
                                       StaleElementReferenceException, \
                                       TimeoutException
from devices.android.android_devices import android_desired_caps
from devices.ios.ios_devices import ios_desired_caps
from conf.conf import SCREENSHOT_PATH
from custom_excepitons.appium_exceptions import AppiumConnectionFailException, InvalidDeviceTypeException
from custom_excepitons.env_variable_exceptions import EnvVariableNotSetException
from utils.classes import SingletonMeta

from conf.conf import TIMEOUT_FIND_LOCATOR


class AppiumDriver(metaclass=SingletonMeta):
    connection = None
    ANDROID = 'android'
    IOS = 'ios'
    desired_caps = None

    if "DEVICE_TYPE" not in os.environ:
        logger.critical(f"Env variable 'device_type' is not set")
        raise EnvVariableNotSetException(f"Env variable 'device_type' is not set")

    if "HUB_URL" not in os.environ:
        logger.critical(f"Env variable 'hub_url' is not set")
        raise EnvVariableNotSetException(f"Env variable 'hub_url' is not set")

    device_type = os.getenv('DEVICE_TYPE')
    logger.info(f'testing for device type {device_type}')

    hub_url = os.getenv('HUB_URL')
    logger.info(f'appium server url is {hub_url}')


    def connect(self, device):

        if self.connection is None:
            if self.device_type.lower() == self.ANDROID:
                try:
                    self.desired_caps = android_desired_caps[device]
                    self.connection = webdriver.Remote(command_executor=self.hub_url,
                                                       desired_capabilities=self.desired_caps)
                except Exception as e:
                    logger.exception(e)
                    raise AppiumConnectionFailException('Could not connect to appium server. '
                                                          'Please check if '
                                                          'appium server is running')

            elif self.device_type.lower() == self.IOS:
                try:
                    self.desired_caps = ios_desired_caps
                    self.connection = webdriver.Remote(command_executor=self.hub_url,
                                                   desired_capabilities=self.desired_caps)
                except Exception as e:
                    raise AppiumConnectionFailException('Could not connect to appium server. '
                                                          'Please check if '
                                                          'appium server is running')
            else:
                logger.critical(f"Invalid device type provided")
                raise InvalidDeviceTypeException("Invalid device type provided")

        return self.connection

    def find_element(self, locator, timeout=TIMEOUT_FIND_LOCATOR):
        ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)
        wait = WebDriverWait(driver=self.connection,
                             timeout=int(timeout),
                             ignored_exceptions=ignored_exceptions)

        try:
            return wait.until(EC.visibility_of_element_located(locator))

        except Exception as e:
            logger.critical("Could not locate element with value: %s" % str(locator))
            raise NoSuchElementException("Could not locate element with value: %s" % str(locator))

    def find_elements(self, locator, timeout=TIMEOUT_FIND_LOCATOR):
        ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)
        wait = WebDriverWait(driver=self.connection, timeout=int(timeout), ignored_exceptions=ignored_exceptions)
        try:
            return wait.until(EC.visibility_of_all_elements_located(locator))
        except TimeoutException as e:
            logger.critical("Could not locate element with value: %s" % str(locator))
            raise NoSuchElementException("Could not locate element with value: %s" % str(locator))

    def tap(self, locator):
        element = self.find_element(locator)
        actions = TouchAction(self.connection)
        actions.tap(element)
        actions.perform()

    def enter_text(self, locator, text):
        self.find_element(locator).clear().send_keys(text)

    def click(self, locator):
        self.find_element(locator).click()

    def get_current_activity(self):
        return self.connection.current_activity

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

    def press_android_back_button(self):
        self.connection.back()

    def get_value_of_edit_text_widget(self, locator):
        self.find_element(locator).get_attribute('value')

    def get_log_type(self):
        return self.connection.log_types

    def get_server_logs(self):
        return self.connection.get_log('server')

    def get_logcat_logs(self):
        return self.connection.get_log('logcat')

    def change_device_orientation(self, orientation='LANDSCAPE'):
        orientation.upper()
        self.connection.orientation = orientation

    def is_app_installed(self, package):
        return self.connection.is_app_installed(package)

    def install_app(self, apk):
        self.connection.install_app(apk)

    def get_app_state(self, package):
        return self.connection.query_app_state(package)

    def launch_app(self):
        self.connection.launch_app()

    def close_app(self):
        self.connection.launch_app()

    def reset_app(self):
        self.connection.reset()

    def remove_app(self, package):
        self.connection.remove_app(package)

    def quit(self):
        self.connection.quit()

    def save_screenshot(self, filename):
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        image_name = filename + '_' + now + '.png'
        filepath = os.path.join(SCREENSHOT_PATH, image_name)

        screenshot_base64 = self.connection.get_screenshot_as_base64()

        image = base64.b64decode(str(screenshot_base64))
        img = Image.open(io.BytesIO(image))
        img.save(filepath, 'png')

    def enter_otp(self, locator, otp):
        self.send_keys_to_multiple_inputs(locator=locator, text=otp)

    def tap_on_filtered_result_on_basis_of_country(self, locator, country):
        filtered_results = self.find_elements(locator)
        limit = len(filtered_results)

        for temp in range(limit):
            if country.lower() == filtered_results[temp].text.lower():
                filtered_results[temp].click()
                return


