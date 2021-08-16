import functools
from conf.conf import logger_test

def exceptions_handler(func):
    @functools.wraps(func)
    def inner_func(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except AttributeError as e:
            logger_test.exception(e)

    return inner_func