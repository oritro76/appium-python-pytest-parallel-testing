class Error(Exception):
    """Base class"""
    pass


class AppiumConnectionFaileExcetipion(Error):
    """Exception showed when loss is not shown in currency conversion calculation"""

    def __init__(self, message):
        self.message = message
