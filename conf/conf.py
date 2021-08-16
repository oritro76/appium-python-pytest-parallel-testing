import os
import sys
from definitions import ROOT_DIR
from loguru import logger


APK_PATH = os.path.join(ROOT_DIR, "data", "apps", "android", "app-debug.apk")
IPA_PATH = ''
APPIUM_SERVER_LOG_PATH = os.path.join(ROOT_DIR, 'logs', 'appium_server', 'server.log')
LOGCAT_LOG_PATH = os.path.join(ROOT_DIR, 'logs', 'logcat', 'logcat.log')
TESTS_LOG_DIR_PATH = os.path.join(ROOT_DIR, 'logs', 'tests')
TESTS_LOG_PATH = os.path.join(ROOT_DIR, 'logs', 'tests', 'tests.log')
SCREENSHOT_PATH = os.path.join(ROOT_DIR, 'screenshots')

APK_PACKAGE_NAME = "app.choco.dummyqa"
APP_ACTIVITY = "SplashScreenActivity"

logger.remove()

logger.add(sys.stderr, level="INFO")

logger.add(sink=APPIUM_SERVER_LOG_PATH,
           filter=lambda record: record["extra"]["appium_server"] == "appium_server",
           level='INFO',
           mode="w")

logger.add(LOGCAT_LOG_PATH,
           filter=lambda record: record["extra"]["logcat"] == "logcat",
           level='INFO',
           mode="w")

logger.add(TESTS_LOG_PATH,
           filter=lambda record: record["extra"]["test"] == "test",
           level='INFO',
           mode="w")

logger_appium_server = logger.bind(appium_server="appium_server")
logger_logcat = logger.bind(logcat="logcat")
logger_test = logger.bind(test="test")
