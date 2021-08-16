import os

from definitions import ROOT_DIR

APK_PATH = os.path.join(ROOT_DIR, "data", "apps", "android", "app-debug.apk")
IPA_PATH = ''
APPIUM_SERVER_LOG_PATH = os.path.join(ROOT_DIR, 'logs', 'appium_server', 'server.log')
LOGCAT_LOG_PATH = os.path.join(ROOT_DIR, 'logs', 'logcat', 'logcat.log')
TESTS_LOG_DIR_PATH = os.path.join(ROOT_DIR, 'logs', 'tests')
SCREENSHOT_PATH = os.path.join(ROOT_DIR, 'screenshots')

APK_PACKAGE_NAME = "app.choco.dummyqa"
APP_ACTIVITY = "SplashScreenActivity"

TIMEOUT_FIND_LOCATOR = 10
