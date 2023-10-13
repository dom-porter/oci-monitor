class ClientException(Exception):
    """ Exception for all types of issues raised but the IaaS providers client """

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class ProviderError(Exception):
    """ Exception default error whilst communicating with the IaaS API """

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
