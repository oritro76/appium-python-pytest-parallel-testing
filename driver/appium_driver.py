from datetime import datetime
import os
import base64
import io

from PIL import Image
from appium import webdriver
from loguru import logger
from devices.android.android_devices import android_desired_caps
from devices.ios.ios_devices import ios_desired_caps
from conf.conf import SCREENSHOT_PATH


class SingletonMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)

        return cls._instances[cls]


class AppiumDriver(metaclass=SingletonMeta):
    connection = None
    ANDROID = 'android'
    IOS = 'ios'

    def connect(self):
        device_type = os.getenv('DEVICE_TYPE', 'android')
        hub_url = os.getenv('HUB_URL', 'http://localhost:4723/wd/hub')

        if self.connection is None:
            if device_type.lower() == self.ANDROID:
                self.connection = webdriver.Remote(command_executor=hub_url, desired_capabilities=android_desired_caps)
            else:
                self.connection = webdriver.Remote(command_executor=hub_url, desired_capabilities=ios_desired_caps)

        return self.connection

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
