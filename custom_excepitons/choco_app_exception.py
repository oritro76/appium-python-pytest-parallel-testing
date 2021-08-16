from custom_excepitons.base_exception import Error


class ButtonTextMismatchException(Error):

    def __init__(self, message):
        self.message = message