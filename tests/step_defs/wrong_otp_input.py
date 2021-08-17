from pytest_bdd import when, then, scenarios, parsers, given, feature
from assertpy import assert_that

from loguru import logger
from data.data_gen import DataGenerator


scenarios('../features/wrong_otp_input.feature')





