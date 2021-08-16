from custom_excepitons.base_excepion import Error


class EnvVariableNotSetException(Error):
    """Exception showed when loss is not shown in currency conversion calculation"""

    def __init__(self, message):
        self.message = message