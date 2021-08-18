from custom_excepitons.base_exception import Error


class AppiumConnectionFailException(Error):

    def __init__(self, message):
        self.message = message


class InvalidDeviceTypeException(Error):

    def __init__(self, message):
        self.message = message
