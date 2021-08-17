import functools
from loguru import logger

def exceptions_handler(func):
    @functools.wraps(func)
    def inner_func(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except AttributeError as e:
            logger.exception(e)

    return inner_func

