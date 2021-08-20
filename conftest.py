from pathlib import Path
from loguru import logger
import pytest
from _pytest.logging import caplog as _caplog
import logging

from driver.appium_driver import AppiumDriver
from conf.conf import TESTS_LOG_DIR_PATH


pytest_plugins = [
    "tests.fixtures.test_helpers"
]


@pytest.fixture(scope='function')
def appium_driver():
    appium_driver = AppiumDriver()
    appium_driver.connect()

    yield appium_driver

    logger.info('Quiting Appium server connection')
    appium_driver.quit()
    logger.info("quit driver session")


@pytest.fixture
def caplog(_caplog):
    class PropogateHandler(logging.Handler):
        def emit(self, record):
            logging.getLogger(record.name).handle(record)

    handler_id = logger.add(PropogateHandler(), format="{message} {extra}", level="TRACE")
    yield _caplog
    logger.remove(handler_id)


@pytest.fixture(autouse=True)
def write_logs(request):
    # put logs in tests/logs
    log_path = Path(TESTS_LOG_DIR_PATH)

    # tidy logs in subdirectories based on test module and class names
    module = request.module
    class_ = request.cls
    name = request.node.name + ".log"

    if module:
        log_path /= module.__name__.replace("tests.", "")
    if class_:
        log_path /= class_.__name__

    log_path.mkdir(parents=True, exist_ok=True)

    # append last part of the name
    log_path /= name

    # enable the logger
    logger.remove()
    logger.configure(handlers=[{"sink": log_path, "level": "TRACE", "mode": "w"}])
    logger.enable("my_package")


def pytest_bdd_before_scenario(request, feature, scenario):
    logger.info(f"feature name: {feature.name}")

    logger.info(f"{scenario.name} started")


def pytest_bdd_after_scenario(request, feature, scenario):
    appium_driver = AppiumDriver()

    logger.info('printing adb log')
    try:
        logcat_logs = appium_driver.get_logcat_logs()
        for log in logcat_logs:
            logger.info(log)
    except AttributeError as e:
        logger.exception(e)
    except Exception as e:
        logger.exception(e)

    logger.info(f"{scenario.name} executed")


def pytest_bdd_before_step_call(request, feature, scenario, step, step_func, step_func_args):
    logger.info(f"{request.node.name} started")


def pytest_bdd_after_step(request, feature, scenario, step, step_func, step_func_args):
    logger.info(f"{request.node.name} executed")


def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):

    logger.info(f"{request.node.name} error happened")
    # logger.info("Taking screenshot")
    # try:
    #     appium_driver.save_screenshot(scenario.name)
    #
    #     appium_driver.close_app()
    # except AttributeError as e:
    #     logger.exception(e)
    # except Exception as e:
    #     logger.exception(e)



