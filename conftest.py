from pathlib import Path
from loguru import logger
import pytest

from driver.appium_driver import AppiumDriver
from conf.conf import logger_logcat, logger_test

def pytest_bdd_before_scenario(request, feature, scenario):
    logger_logcat.info(f"feature name: {feature.name}")

    logger_logcat.info(f"{scenario.name} started")

    logger_test.info(f"{scenario.name} started")


def pytest_bdd_after_scenario(request, feature, scenario):
    appium_driver = AppiumDriver()

    logcat = appium_driver.get_logcat_logs()
    for log in logcat:
        logger_logcat.info(log)

    logger_logcat.info(f"{scenario.name} executed")
    logger_test.info(f"{scenario.name} executed")


def pytest_bdd_before_step_call(request, feature, scenario, step, step_func, step_func_args):
    logger_logcat.info(f"{request.node.name} started")


def pytest_bdd_after_step(request, feature, scenario, step, step_func, step_func_args):
    logger_logcat.info(f"{request.node.name} executed")


def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    appium_driver = AppiumDriver()
    appium_driver.save_screenshot(scenario.name)

    appium_driver.reset_app()

    logger_logcat.info(f"{request.node.name} exception happened")

    logger_test.critical(f"{exception}")
